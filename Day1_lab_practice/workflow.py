"""System 2: Rule-based event registration workflow."""

import re
from config import EVENT_FEES, QUESTIONS


def workflow(question):

    codes = re.findall(
        r"[A-Z]{2,4}\d{3}",
        question.upper()
    )

    fees = [
        EVENT_FEES[code]
        for code in codes
        if code in EVENT_FEES
    ]

    if not fees:
        return "Sorry, I can only answer questions about event registration fees."

    text = question.lower()

    if "total" in text:

        total = sum(fees)

        percent = re.search(
            r"(\d+)\s*%",
            text
        )

        if "discount" in text and percent:

            total = total * (
                1 - int(percent.group(1)) / 100
            )

        return f"Total registration fee: Rs. {total:,.0f}"

    if len(fees) == 1:

        return f"Registration fee: Rs. {fees[0]:,}"

    if "more expensive" in text or "higher" in text:

        difference = abs(fees[0] - fees[1])

        if fees[0] > fees[1]:
            return f"The first event is more expensive by Rs. {difference:,}."

        elif fees[1] > fees[0]:
            return f"The second event is more expensive by Rs. {difference:,}."

        else:
            return "Both events have the same registration fee."

    return "Sorry, I do not have a rule for this type of question."


if __name__ == "__main__":

    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW ===\n")

    for question in QUESTIONS:

        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)