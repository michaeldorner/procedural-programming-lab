from datetime import date


# Student template
def format_date_iso(
    value: date,
) -> str:
    pass


def format_date_german(
    value: date,
) -> str:
    pass


# Basic solution
def format_date_iso(
    value: date,
) -> str:
    return value.isoformat()


def format_date_german(
    value: date,
) -> str:
    return value.strftime("%d.%m.%Y")


# Excellent solution for bonus tests
def format_date_iso(
    value: date,
) -> str:
    return value.isoformat()


def format_date_german(
    value: date,
) -> str:
    return value.strftime("%d.%m.%Y")
