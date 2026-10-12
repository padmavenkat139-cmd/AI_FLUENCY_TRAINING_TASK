"""Self-consistency experiment."""

import sys
from pathlib import Path
from collections import Counter

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config import client, MODEL


QUESTION = """
A college has 120 students.

40% choose Python.
35% choose Java.
The remaining students choose Web Development.

How many students choose Web Development?

Give the final numerical answer clearly.
"""


print("\n" + "=" * 60)
print("SELF-CONSISTENCY EXPERIMENT")
print("=" * 60)

answers = []

for run in range(5):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Solve the problem carefully. "
                    "Give a short explanation and clearly state "
                    "the final numerical answer."
                )
            },
            {
                "role": "user",
                "content": QUESTION
            }
        ],
        temperature=0.8
    )

    answer = response.choices[0].message.content
    answers.append(answer)

    print(f"\n{'=' * 20} RUN {run + 1} {'=' * 20}")
    print(answer)


print("\n" + "=" * 60)
print("SELF-CONSISTENCY SUMMARY")
print("=" * 60)

print("""
Expected calculation:

Python = 40% of 120 = 48

Java = 35% of 120 = 42

Web Development = 120 - 48 - 42

Web Development = 30 students

Expected final answer: 30 students
""")

print(f"Number of runs: {len(answers)}")
print("Temperature used: 0.8")