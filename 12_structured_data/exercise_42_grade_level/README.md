# Exercise 42: Grade Level

## Objective

Classify scores into grade levels.

## Tasks

Implement the following function in `solution.py`:

```python
from enum import Enum


class GradeLevel(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    PASS = "pass"
    FAIL = "fail"

def grade_level(
    score: int,
) -> GradeLevel:
    pass
```

## Examples

```python
grade_level(95)
```

returns

```python
GradeLevel.EXCELLENT
```
```python
grade_level(75)
```

returns

```python
GradeLevel.GOOD
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
