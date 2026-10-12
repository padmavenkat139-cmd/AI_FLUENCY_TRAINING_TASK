
"""Demonstrate structured JSON output."""

import json
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "Day1_lab_practice")
)

from config import client, MODEL, banner

SCHEMA = {
    "type": "object",
    "properties": {
        "book_code": {
            "type": "string",
            "enum": ["PY101", "DB201", "AI301"],
        },
        "wants_discount": {"type": "boolean"},
        "needs_price_lookup": {"type": "boolean"},
    },
    "required": [
        "book_code",
        "wants_discount",
        "needs_price_lookup",
    ],
    "additionalProperties": False,
}

QUESTION = (
    "What is the price of Python Programming after a 10% discount?"
)


def ask(response_format, label):
    print(f"\n--- {label} ---")

    try:
        reply = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Extract the request into JSON with keys "
                        "book_code, wants_discount, and "
                        "needs_price_lookup. "
                        "PY101 means Python Programming. "
                        "Return JSON only."
                    ),
                },
                {"role": "user", "content": QUESTION},
            ],
            temperature=0,
            response_format=response_format,
        )

        output = reply.choices[0].message.content.strip()
        print("Raw:", output)
        print("Parsed:", json.loads(output))

    except Exception as error:
        print(f"Not supported or failed: {type(error).__name__}: {error}")


if __name__ == "__main__":
    banner("STRUCTURED OUTPUTS")

    ask(None, "1. Free-form response")

    ask(
        {"type": "json_object"},
        "2. JSON mode",
    )

    ask(
        {
            "type": "json_schema",
            "json_schema": {
                "name": "bookstore_query",
                "schema": SCHEMA,
                "strict": True,
            },
        },
        "3. Strict JSON schema mode",
    )