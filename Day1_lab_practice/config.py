"""Shared configuration for the College Event Registration Assistant."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "ollama").strip().lower()

if PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

elif PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

elif PROVIDER == "huggingface":
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'."
    )

if not API_KEY:
    raise SystemExit(
        f"No API key found for PROVIDER={PROVIDER}."
    )

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

# Private college event data
EVENT_FEES = {
    "PY101": 800,
    "AI202": 1200,
    "WEB303": 1000
}

QUESTIONS = [
    "What is the registration fee for AI202?",
    "What is the total fee for PY101 and AI202 after a 10% student discount?",
    "Is WEB303 more expensive than PY101, and by how much?",
    "Write a two-line welcome message for students joining the workshops."
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | model: {MODEL} ===\n"
    )