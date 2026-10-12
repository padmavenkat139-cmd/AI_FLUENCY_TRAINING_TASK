
"""Validate tool arguments before executing a function."""

TYPES = {
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "array": list,
    "object": dict,
}


def validate_arguments(arguments, schema):
    if not isinstance(arguments, dict):
        return "Arguments must be a JSON object."

    properties = schema.get("properties", {})

    for name in schema.get("required", []):
        if name not in arguments:
            return (
                f"Missing required argument '{name}'. "
                f"Expected: {', '.join(properties)}."
            )

    if schema.get("additionalProperties") is False:
        extra = [key for key in arguments if key not in properties]
        if extra:
            return (
                f"Unexpected argument(s): {', '.join(extra)}. "
                f"Allowed: {', '.join(properties)}."
            )

    for name, value in arguments.items():
        rule = properties.get(name, {})
        expected = TYPES.get(rule.get("type"))

        if expected and (
            not isinstance(value, expected)
            or (rule.get("type") == "integer" and type(value) is not int)
            or (rule.get("type") == "number" and type(value) is bool)
        ):
            return (
                f"Argument '{name}' must be a {rule['type']}, "
                f"but got {type(value).__name__}."
            )

        if "enum" in rule and value not in rule["enum"]:
            return (
                f"Argument '{name}' must be one of "
                f"{rule['enum']}, got {value!r}."
            )

    return None


if __name__ == "__main__":
    from tools_v2 import SCHEMAS

    schema = SCHEMAS["get_book_price"]

    cases = [
        {"book_code": "PY101"},
        {},
        {"book_code": 101},
        {"book_code": "ME404"},
        {"book_code": "PY101", "year": 2026},
    ]

    for case in cases:
        error = validate_arguments(case, schema)
        print(f"{case} -> {error or 'OK'}")