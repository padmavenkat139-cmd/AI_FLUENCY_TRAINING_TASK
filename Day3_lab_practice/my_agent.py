import sys
from pathlib import Path
from dotenv import load_dotenv

# Use the existing Day1 configuration and environment
DAY1_FOLDER = Path(
    r"C:\Users\padma\OneDrive\Desktop\AI_assigned_task\Day1_lab_practice"
)

load_dotenv(DAY1_FOLDER / ".env")
sys.path.insert(0, str(DAY1_FOLDER))

from config import client, MODEL
from my_tools import lookup_bus_schedule


# Tool schema shown to the LLM
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_bus_schedule",
            "description": (
                "Look up the private college bus schedule "
                "when the user asks about a bus route."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "route": {
                        "type": "string",
                        "description": "Bus route code such as B1, B2, B3 or B4."
                    }
                },
                "required": ["route"]
            }
        }
    }
]


# Same question that we will compare with the plain LLM
question = (
    "What is the departure time and final stop of College Bus Route B4?"
)

print("\nQUESTION:")
print(question)

# First: ask the LLM
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    tools=TOOLS,
    tool_choice="auto",
    temperature=0
)

message = response.choices[0].message

# Check whether the LLM decided to use the tool
if message.tool_calls:

    print("\nTOOL CALL:")
    
    tool_call = message.tool_calls[0]
    print("Tool:", tool_call.function.name)
    print("Arguments:", tool_call.function.arguments)

    # Get the route requested by the LLM
    import json

    arguments = json.loads(tool_call.function.arguments)
    route = arguments["route"]

    # Run our actual tool
    tool_result = lookup_bus_schedule(route)

    print("\nTOOL RESULT:")
    print(tool_result)

    # Send the tool result back to the LLM
    messages = [
        {
            "role": "user",
            "content": question
        },
        message,
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": tool_result
        }
    ]

    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    print("\nFINAL ANSWER:")
    print(final_response.choices[0].message.content)

else:
    print("\nNO TOOL CALL WAS MADE.")
    print("\nLLM ANSWER:")
    print(message.content)