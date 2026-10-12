
"""Test the bookstore agent with deliberately broken tool calls."""

import json
from robust_agent import handle_tool_call


class FakeFunction:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class FakeCall:
    def __init__(self, name, arguments, call_id="call_test"):
        self.id = call_id
        self.type = "function"
        self.function = FakeFunction(name, arguments)


FAULTS = [
    ("Valid call",
     FakeCall("get_book_price", '{"book_code": "PY101"}')),

    ("Invalid JSON",
     FakeCall("get_book_price", '{"book_code": "PY101"')),

    ("Unknown tool",
     FakeCall("send_email", '{"to": "customer@example.com"}')),

    ("Missing argument",
     FakeCall("get_book_price", '{}')),

    ("Wrong argument type",
     FakeCall("get_book_price", '{"book_code": 101}')),

    ("Invalid book code",
     FakeCall("get_book_price", '{"book_code": "ME404"}')),

    ("Extra argument",
     FakeCall(
         "get_book_price",
         '{"book_code": "PY101", "year": 2026}'
     )),

    ("Unsafe calculation",
     FakeCall(
         "calculator",
         json.dumps({"expression": "__import__('os').system('dir')"})
     )),

    ("Empty arguments",
     FakeCall("calculator", "")),

    ("JSON array instead of object",
     FakeCall("get_book_price", '["PY101"]')),
]


if __name__ == "__main__":
    print("=" * 75)

    for label, call in FAULTS:
        result = handle_tool_call(call, log=False)
        print(f"{label:<30} -> {result[:100]}")

    print("=" * 75)
    print("Fault testing completed.")