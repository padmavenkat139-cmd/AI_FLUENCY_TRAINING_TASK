
import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = (
    "You are a Python Programming Study Assistant. "
    "Explain concepts in simple English and give short examples."
)

PROMPT = (
    "Explain what a Python variable is. "
    "Use simple English and give one short example."
)


def make_request(stream=False):
    if not API_KEY:
        raise ValueError("GROQ_API_KEY is missing from your .env file.")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PROMPT},
        ],
        "temperature": 0.2,
        "stream": stream,
    }

    return requests.post(
        URL,
        headers=headers,
        json=payload,
        stream=stream,
        timeout=180,
    )


def run_non_streaming():
    print("\n=== GROQ NON-STREAMING ===")

    start = time.perf_counter()

    with make_request(stream=False) as response:
        response.raise_for_status()
        data = response.json()

    elapsed = time.perf_counter() - start
    answer = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})

    print("Answer:", answer)
    print(f"Total response time: {elapsed:.3f} seconds")
    print("Completion tokens:", usage.get("completion_tokens", "Not reported"))


def run_streaming():
    print("\n=== GROQ STREAMING ===")

    start = time.perf_counter()
    first_token_time = None
    pieces = []

    with make_request(stream=True) as response:
        response.raise_for_status()

        for line in response.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data:"):
                continue

            content = line[len("data:"):].strip()

            if content == "[DONE]":
                break

            import json
            event = json.loads(content)

            choices = event.get("choices", [])
            if not choices:
                continue

            piece = choices[0].get("delta", {}).get("content", "")

            if piece:
                if first_token_time is None:
                    first_token_time = time.perf_counter()

                pieces.append(piece)
                print(piece, end="", flush=True)

    end = time.perf_counter()
    print()

    if first_token_time is not None:
        ttft = first_token_time - start
        print(f"TTFT: {ttft:.3f} seconds")
    else:
        print("TTFT: No text received")

    print(f"Total streaming time: {end - start:.3f} seconds")
    print("Streaming characters received:", len("".join(pieces)))


if __name__ == "__main__":
    try:
        print("Provider: Groq")
        print("Model:", MODEL)

        run_non_streaming()
        run_streaming()

    except requests.RequestException as error:
        print("API request failed:", error)
    except (ValueError, KeyError) as error:
        print("Configuration or response error:", error)
