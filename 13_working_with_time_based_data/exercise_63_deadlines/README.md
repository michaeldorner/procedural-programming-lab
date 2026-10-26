# Exercise 63: Deadlines

## Objective

Determine whether a due date is overdue.

## Tasks

Implement the following function in `solution.py`:

```python
from datetime import date

def is_overdue(
    due_date: date,
    today: date,
) -> bool:
    pass
```

## Examples

```python
is_overdue(date(2026, 1, 1), date(2026, 1, 2))
```

returns

```python
True
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
