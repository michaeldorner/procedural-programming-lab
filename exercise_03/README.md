# Exercise 03: Circle Calculations

## Objective

Calculate area and circumference of a circle.

## Tasks

Implement the following functions in `solution.py`:

```python
import math

def circle_area(
    radius: float,
) -> float:
    pass

def circle_circumference(
    radius: float,
) -> float:
    pass
```

## Examples

```python
circle_area(1.0)
```

returns

```python
3.141592653589793
```
```python
circle_circumference(1.0)
```

returns

```python
6.283185307179586
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.

## Bonus

A radius of `0.0` is valid.

Negative radii are not meaningful for circles.

The excellent solution should raise a `ValueError` if the radius is negative.

The excellent solution should also reject non-finite values such as:

- `float("nan")`
- `float("inf")`
- `float("-inf")`

Floating-point results do not need to be rounded. The tests allow small floating-point differences where appropriate.
