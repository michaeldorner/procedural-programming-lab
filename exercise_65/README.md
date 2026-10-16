# Exercise 65: Working Hours

## Objective

Determine whether a time is within working hours.

## Tasks

Implement the following function in `solution.py`:

```python
from datetime import time

def is_working_hour(
    value: time,
) -> bool:
    pass
```

## Examples

```python
is_working_hour(time(10, 0))
```

returns

```python
True
```
```python
is_working_hour(time(18, 0))
```

returns

```python
False
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
