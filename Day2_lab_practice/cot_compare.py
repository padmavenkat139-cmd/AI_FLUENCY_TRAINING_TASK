"""Compare direct prompting with step-by-step reasoning."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config import client, MODEL


QUESTION = """
A farmer has:
- 2 acres of tomato, requiring 1200 litres of water per acre
- 3 acres of rice, requiring 2000 litres of water per acre
- 1 acre of cotton, requiring 1500 litres of water per acre

Calculate:
1. The total water requirement.
2. The amount of water saved with a 15% water-saving method.
3. The final water requirement after the saving.
"""


def ask_model(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


print("\n" + "=" * 60)
print("WITHOUT CoT - DIRECT PROMPTING")
print("=" * 60)

without_cot = ask_model(
    QUESTION
    + "\nGive only the final answer. Do not explain the calculation."
)

print(without_cot)


print("\n" + "=" * 60)
print("WITH CoT - STEP-BY-STEP REASONING")
print("=" * 60)

with_cot = ask_model(
    QUESTION
    + """
Solve the problem carefully.
Give a concise calculation showing the important steps,
then give the final answer.
"""
)

print(with_cot)


print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

print("""
Without CoT:
- Gives the answer directly.
- Does not show calculation steps.

With CoT:
- Shows the calculation steps.
- Makes the solution easier to follow.
""")