# Exercise 10: Triangle Type

## Objective

Implement a function that classifies a triangle based on the lengths of its three sides.

## Tasks

Implement the following function in `solution.py`:

```python
def triangle_type(
    a: float,
    b: float,
    c: float,
) -> str:
    pass
```

## Triangle Types

Use the following classifications:

```text
equilateral    all three sides have the same length
isosceles      exactly two sides have the same length
scalene        all three sides have different lengths
invalid        the side lengths cannot form a triangle
```

## Triangle Rule

Three side lengths can form a valid triangle if each pair of sides is longer than the remaining side:

```text
a + b > c
a + c > b
b + c > a
```

## Examples

```python
triangle_type(
    3.0,
    3.0,
    3.0,
)
```

returns

```python
"equilateral"
```

```python
triangle_type(
    3.0,
    3.0,
    4.0,
)
```

returns

```python
"isosceles"
```

```python
triangle_type(
    3.0,
    4.0,
    5.0,
)
```

returns

```python
"scalene"
```

```python
triangle_type(
    1.0,
    2.0,
    3.0,
)
```

returns

```python
"invalid"
```

## Notes

- Return the triangle type as a string.
- Do not print the result inside the function.
- Do not change the function signature.
- Side lengths must be positive numbers.

## Side Length Validation

A side length is invalid if:

- it is less than or equal to `0`,
- it is `nan`,
- it is `inf` or `-inf`,
- it is not a number.

For invalid side lengths, raise a `ValueError`.

If the side lengths are finite and positive but cannot form a triangle, return `"invalid"`.
