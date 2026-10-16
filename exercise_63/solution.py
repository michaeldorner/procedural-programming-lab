from datetime import date


# Student template
def is_overdue(
    due_date: date,
    today: date,
) -> bool:
    pass


# Basic solution
def is_overdue(
    due_date: date,
    today: date,
) -> bool:
    return today > due_date


# Excellent solution for bonus tests
def is_overdue(
    due_date: date,
    today: date,
) -> bool:
    return today > due_date
