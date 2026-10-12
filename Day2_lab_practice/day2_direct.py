"""Direct prompting approach for the Smart Agriculture scenario."""

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

Give the final answer clearly.
"""


response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful agriculture calculation assistant."
        },
        {
            "role": "user",
            "content": QUESTION
        }
    ],
    temperature=0
)

print("\n===== DIRECT PROMPTING =====\n")
print(response.choices[0].message.content)