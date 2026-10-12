
"""Online Bookstore Assistant: tools and strict schemas."""

import ast
import operator

BOOK_PRICES = {
    "PY101": 500,
    "DB201": 700,
    "AI301": 900,
}

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def get_book_price(book_code: str) -> str:
    """Return the price of a book."""
    code = book_code.strip().upper()
    price = BOOK_PRICES.get(code)

    if price is None:
        return (
            f"Unknown book code: {code}. "
            f"Valid codes: {', '.join(BOOK_PRICES)}"
        )

    return str(price)


def _evaluate(node):
    """Safely evaluate basic arithmetic expressions."""
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.left), _evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.operand))

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""
    try:
        return str(_evaluate(ast.parse(expression, mode="eval").body))
    except Exception as error:
        return f"Calculator error: {error}. Use numbers and + - * / only."


TOOL_FUNCTIONS = {
    "get_book_price": get_book_price,
    "calculator": calculator,
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_book_price",
            "description": (
                "Get the price of one book. "
                "Valid codes: PY101, DB201, AI301."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "book_code": {
                        "type": "string",
                        "enum": ["PY101", "DB201", "AI301"],
                        "description": "The book code",
                    }
                },
                "required": ["book_code"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Calculate arithmetic expressions using numbers, "
                "+, -, *, / and parentheses."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"],
                "additionalProperties": False,
            },
        },
    },
]

SCHEMAS = {
    tool["function"]["name"]: tool["function"]["parameters"]
    for tool in TOOLS
}