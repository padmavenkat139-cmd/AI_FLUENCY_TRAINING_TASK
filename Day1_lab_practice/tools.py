"""Tools available to the AI agent."""

import ast
import operator

from config import EVENT_FEES


def get_event_fee(event_code: str) -> str:
    """Look up the registration fee for an event."""

    fee = EVENT_FEES.get(
        event_code.strip().upper()
    )

    if fee is not None:
        return str(fee)

    return f"Unknown event code: {event_code}"


# Safe calculator
_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}


def _evaluate(node):

    if isinstance(node, ast.Constant):

        if isinstance(node.value, (int, float)):
            return node.value

    if isinstance(node, ast.BinOp):

        if type(node.op) in _OPS:

            return _OPS[type(node.op)](
                _evaluate(node.left),
                _evaluate(node.right)
            )

    if isinstance(node, ast.UnaryOp):

        if type(node.op) in _OPS:

            return _OPS[type(node.op)](
                _evaluate(node.operand)
            )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:

    try:

        result = _evaluate(
            ast.parse(
                expression,
                mode="eval"
            ).body
        )

        return str(result)

    except Exception as error:

        return f"Calculator error: {error}"


TOOL_FUNCTIONS = {
    "get_event_fee": get_event_fee,
    "calculator": calculator
}


TOOLS = [

    {
        "type": "function",

        "function": {
            "name": "get_event_fee",

            "description":
                "Get the registration fee in rupees "
                "for a single college event code.",

            "parameters": {
                "type": "object",

                "properties": {
                    "event_code": {
                        "type": "string"
                    }
                },

                "required": ["event_code"]
            }
        }
    },

    {
        "type": "function",

        "function": {
            "name": "calculator",

            "description":
                "Evaluate arithmetic expressions "
                "using + - * / and brackets.",

            "parameters": {
                "type": "object",

                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },

                "required": ["expression"]
            }
        }
    }
]


if __name__ == "__main__":

    print(
        "get_event_fee('AI202') ->",
        get_event_fee("AI202")
    )

    print(
        "calculator('(800 + 1200) * 0.9') ->",
        calculator("(800 + 1200) * 0.9")
    )

    print(
        "calculator('1000 - 800') ->",
        calculator("1000 - 800")
    )