# Exercise 01: Rectangles

## Objective

Calculate the area and perimeter of a rectangle.

## Tasks

Implement the following functions in `solution.py`:

```python
def rectangle_area(
    width: float,
    height: float,
) -> float:
    pass

def rectangle_perimeter(
    width: float,
    height: float,
) -> float:
    pass
```

## Examples

```python
rectangle_area(3.0, 4.0)
```

returns

```python
12.0
```
```python
rectangle_perimeter(3.0, 4.0)
```

returns

```python
14.0
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.

## Bonus

Negative dimensions are not meaningful for rectangles.

To get the bonus, raise a `ValueError` if `width` or `height` is negative.
