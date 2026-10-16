# Exercise 64: Date Formatting

## Objective

Format dates as strings.

## Tasks

Implement the following functions in `solution.py`:

```python
from datetime import date

def format_date_iso(
    value: date,
) -> str:
    pass

def format_date_german(
    value: date,
) -> str:
    pass
```

## Examples

```python
format_date_iso(date(2026, 7, 14))
```

returns

```python
'2026-07-14'
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
