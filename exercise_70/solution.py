# Student template
def expense_total(
    expenses: list[dict[str,
    float]],
) -> float:
    pass


# Basic solution
def expense_total(
    expenses: list[dict[str,
    float]],
) -> float:
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total


# Excellent solution for bonus tests
def expense_total(
    expenses: list[dict[str,
    float]],
) -> float:
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total
