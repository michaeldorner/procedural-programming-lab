from datetime import date

def format_date_iso(
    value: date,
) -> str:
    return value.isoformat()


def format_date_german(
    value: date,
) -> str:
    return value.strftime("%d.%m.%Y")
