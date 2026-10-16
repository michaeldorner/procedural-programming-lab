# Exercise 39: Traffic Light

## Objective

Determine whether pedestrians can cross.

## Tasks

Implement the following function in `solution.py`:

```python
from enum import Enum


class TrafficLight(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

def can_cross(
    light: TrafficLight,
) -> bool:
    pass
```

## Examples

```python
can_cross(TrafficLight.GREEN)
```

returns

```python
True
```
```python
can_cross(TrafficLight.RED)
```

returns

```python
False
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
