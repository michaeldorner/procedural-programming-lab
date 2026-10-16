from datetime import date


# Student template
def days_between(
    start: date,
    end: date,
) -> int:
    pass


# Basic solution
def days_between(
    start: date,
    end: date,
) -> int:
    return (end - start).days


# Excellent solution for bonus tests
def days_between(
    start: date,
    end: date,
) -> int:
    return (end - start).days
