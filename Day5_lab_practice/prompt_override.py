import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

URL = "https://api.groq.com/openai/v1/chat/completions"


def ask_groq(system_prompt, user_prompt):
    if not API_KEY:
        print("Error: GROQ_API_KEY is missing from your .env file.")
        return

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 200
    }

    print("Sending request to Groq...")
    start = time.time()

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        data = response.json()
        answer = data["choices"][0]["message"]["content"]

        print(f"Response time: {time.time() - start:.2f} seconds")
        print("\n=== MODEL RESPONSE ===")
        print(answer)

    except requests.exceptions.RequestException as error:
        print("Groq request failed:", error)


system_prompt = (
    "You are a beginner-friendly Python tutor. "
    "Explain concepts in simple English and give a short example."
)

user_prompt = "Explain Python variables in simple English."

print("=== PROGRAM-SUPPLIED SYSTEM PROMPT ===")
ask_groq(system_prompt, user_prompt)
