# Exercise 66: Appointment Conflicts

## Objective

Determine whether two appointments overlap.

## Tasks

Implement the following function in `solution.py`:

```python
from datetime import datetime

def appointments_overlap(
    start_a: datetime,
    end_a: datetime,
    start_b: datetime,
    end_b: datetime,
) -> bool:
    pass
```

## Examples

```python
appointments_overlap(datetime(2026, 1, 1, 9, 0), datetime(2026, 1, 1, 10, 0), datetime(2026, 1, 1, 9, 30), datetime(2026, 1, 1, 10, 30))
```

returns

```python
True
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
