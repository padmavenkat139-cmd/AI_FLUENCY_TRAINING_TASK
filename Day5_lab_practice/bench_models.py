
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").lower()
PROMPTS = [
    (
        "Variable explanation",
        "Explain a Python variable in simple English and give one example."
    ),
    (
        "Rules test",
        "Explain a Python list in exactly two sentences. "
        "Do not use bullet points."
    ),
    (
        "Repeated prompt",
        "Explain a Python variable in simple English and give one example."
    ),
]


def ask_ollama(prompt):
    base_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "day5-study-assistant")

    start = time.perf_counter()
    response = requests.post(
        f"{base_url}/api/chat",
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        },
        timeout=180,
    )
    response.raise_for_status()
    data = response.json()
    elapsed = time.perf_counter() - start

    return (
        data.get("message", {}).get("content", ""),
        elapsed,
        data.get("eval_count", 0),
        data.get("eval_duration", 0),
        data.get("load_duration", 0),
    )


def ask_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing from .env.")

    start = time.perf_counter()
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a beginner-friendly Python Programming "
                        "Study Assistant. Follow the user's instructions."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        },
        timeout=180,
    )
    response.raise_for_status()
    data = response.json()
    elapsed = time.perf_counter() - start

    answer = data["choices"][0]["message"]["content"]
    tokens = data.get("usage", {}).get("completion_tokens", 0)

    return answer, elapsed, tokens, 0, 0


if __name__ == "__main__":
    ask = ask_ollama if PROVIDER == "ollama" else ask_groq

    print("=" * 70)
    print("DAY 5 MODEL BENCHMARK")
    print("Provider:", PROVIDER)
    print("=" * 70)

    for label, prompt in PROMPTS:
        print(f"\nTEST: {label}")
        print("Prompt:", prompt)

        try:
            answer, elapsed, tokens, eval_ns, load_ns = ask(prompt)
            speed = (
                tokens / (eval_ns / 1_000_000_000)
                if eval_ns > 0 else 0
            )

            print(f"Total response time: {elapsed:.3f} seconds")
            print("Completion tokens:", tokens or "not reported")

            if speed:
                print(f"Generation speed: {speed:.2f} tokens/second")
            else:
                print("Generation speed: not available from this response")

            if load_ns:
                print(f"Model load time: {load_ns / 1_000_000:.2f} ms")
            else:
                print("Model load time: not reported")

            print("Answer:")
            print(answer)

        except (requests.RequestException, ValueError, KeyError) as exc:
            print("Test failed:", exc)
