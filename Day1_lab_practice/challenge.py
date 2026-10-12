from tools import calculator, get_event_fee


def challenge():

    print("\n===== CHALLENGE =====")

    budget = 1900

    workshops = {
        "PY101": "Python Workshop",
        "AI202": "AI Workshop",
        "WEB303": "Web Development Workshop"
    }

    print(f"Your budget: Rs. {budget}")
    print("Available workshops:")

    for code, name in workshops.items():

        fee = get_event_fee(code)

        print(
            f"{code} - {name} - Rs. {fee}"
        )

    print("\nPossible combinations within your budget:")

    codes = list(workshops.keys())

    for i in range(len(codes)):

        for j in range(i + 1, len(codes)):

            fee1 = float(get_event_fee(codes[i]))
            fee2 = float(get_event_fee(codes[j]))

            total = float(
                calculator(
                    f"{fee1} + {fee2}"
                )
            )

            if total <= budget:

                print(
                    f"{codes[i]} + {codes[j]} = "
                    f"Rs. {total:.0f}"
                )


if __name__ == "__main__":
    challenge()