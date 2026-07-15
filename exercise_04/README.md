# Exercise 04: Distance Between Points

## Objective

Implement a function that calculates the distance between two points in a two-dimensional coordinate system.

## Tasks

Implement the following function in `solution.py`:

```python
def distance(
    point_a: tuple[float, float],
    point_b: tuple[float, float],
) -> float:
    pass
```

## Formula

For two points

```text
A = (x1, y1)
B = (x2, y2)
```

the distance is calculated as:

```text
distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

## Examples

```python
distance(
    (0.0, 0.0),
    (3.0, 4.0),
)
```

returns

```python
5.0
```

```python
distance(
    (1.0, 1.0),
    (1.0, 1.0),
)
```

returns

```python
0.0
```

## Notes

- A point is represented as a tuple with two numeric values.
- The first value is the x-coordinate.
- The second value is the y-coordinate.
- Negative coordinates are valid.
- Return the calculated value.
- Do not print the result inside the function.
- Do not change the function signature.

## Bonus

The excellent solution should also handle invalid points.

A point is invalid if:

- it does not contain exactly two coordinates,
- one of its coordinates is `nan`,
- one of its coordinates is `inf` or `-inf`.

For invalid points, raise a `ValueError`.
