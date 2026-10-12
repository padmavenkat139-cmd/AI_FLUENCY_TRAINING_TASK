
"""Robust Online Bookstore Assistant."""

import json
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "Day1_lab_practice")
)

from config import client, MODEL

from tools_v2 import TOOLS, TOOL_FUNCTIONS, SCHEMAS
from validate import validate_arguments

SYSTEM_PROMPT = """
You are an online bookstore assistant.
Never guess a book price. Always call get_book_price.
Use calculator for every arithmetic calculation.
Book codes: PY101, DB201, AI301.
Prices: PY101 = Rs. 500, DB201 = Rs. 700,
AI301 = Rs. 900.
A 10% discount means multiplying the total by 0.9.
Answer clearly in Indian rupees.
"""

MAX_TOKENS = 500
REPEAT_LIMIT = 3


def handle_tool_call(call, log=True):
    name = call.function.name
    raw = call.function.arguments or "{}"

    # 1. Validate JSON syntax.
    try:
        arguments = json.loads(raw)
    except json.JSONDecodeError as error:
        return f"Argument error: invalid JSON ({error})."

    # 2. Check whether the tool exists.
    function = TOOL_FUNCTIONS.get(name)
    if function is None:
        return (
            f"Unknown tool: {name}. "
            f"Available tools: {', '.join(TOOL_FUNCTIONS)}."
        )

    # 3. Validate arguments against the schema.
    problem = validate_arguments(arguments, SCHEMAS[name])
    if problem:
        return f"Argument error: {problem}"

    # 4. Execute safely and return a message.
    try:
        result = str(function(**arguments))
    except Exception as error:
        result = f"Tool error: {type(error).__name__}: {error}"

    if log:
        print(f"    {name}({arguments}) -> {result[:100]}")

    return result


def agent(question, max_steps=6, verbose=True):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    seen = {}
    max_tokens = MAX_TOKENS

    for step in range(1, max_steps + 1):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0,
            max_tokens=max_tokens,
        )

        choice = response.choices[0]
        message = choice.message

        if choice.finish_reason == "length":
            if max_tokens >= 2000:
                return "Stopped: reply still truncated at 2000 tokens."

            max_tokens = min(max_tokens * 2, 2000)

            if verbose:
                print(f"Step {step}: retrying with {max_tokens} tokens")

            continue

        if not message.tool_calls:
            return (message.content or "").strip()

        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments,
                    },
                }
                for call in message.tool_calls
            ],
        })

        if verbose:
            print(f"Step {step}: {len(message.tool_calls)} tool call(s)")

        for call in message.tool_calls:
            signature = (call.function.name, call.function.arguments)
            seen[signature] = seen.get(signature, 0) + 1

            if seen[signature] >= REPEAT_LIMIT:
                return (
                    f"Stopped: {call.function.name} repeated the same "
                    f"arguments {REPEAT_LIMIT} times."
                )

            result = handle_tool_call(call, log=verbose)

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result,
            })

    return "Stopped: maximum steps reached."

if __name__ == "__main__":
    print("=" * 75)
    print("ONLINE BOOKSTORE ASSISTANT")
    print("=" * 75)
    
    question = input("Enter your question: ")
    agent(question)
   


    questions = [
        "Find the total price of PY101 and DB201 after a 10% discount.",
        "Is AI301 more expensive than PY101, and by how much?",
        "What is the price of book ME404?",
        "Give a one-line welcome message for bookstore customers.",
    ]

    for question in questions:
        print("\nQ:", question)
        print("A:", agent(question))