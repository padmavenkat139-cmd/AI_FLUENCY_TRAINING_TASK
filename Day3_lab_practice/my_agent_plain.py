import sys
from pathlib import Path
from dotenv import load_dotenv

# Use the existing Day1 configuration
DAY1_FOLDER = Path(
    r"C:\Users\padma\OneDrive\Desktop\AI_assigned_task\Day1_lab_practice"
)

load_dotenv(DAY1_FOLDER / ".env")
sys.path.insert(0, str(DAY1_FOLDER))

from config import client, MODEL


# Same question used in my_agent.py
question = (
    "Write a one-line message reminding college students "
    "to arrive at the bus stop on time."
)


print("\nQUESTION:")
print(question)

# Ask the LLM directly without any tool
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)

print("\nPLAIN LLM ANSWER:")
print(response.choices[0].message.content)