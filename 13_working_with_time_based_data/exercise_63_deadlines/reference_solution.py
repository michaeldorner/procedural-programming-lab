from datetime import date

def is_overdue(
    due_date: date,
    today: date,
) -> bool:
    return today > due_date
