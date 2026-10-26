# Exercise 09: Minimum of Three

## Objective

Implement a function that returns the smallest of three integer values.

## Tasks

Implement the following function in `solution.py`:

```python
def minimum_of_three(
    a: int,
    b: int,
    c: int,
) -> int:
    pass
```

## Examples

```python
minimum_of_three(
    3,
    1,
    2,
)
```

returns

```python
1
```

```python
minimum_of_three(
    7,
    7,
    7,
)
```

returns

```python
7
```

## Notes

- Return the smallest value.
- Do not print the result inside the function.
- Do not change the function signature.
- Equal values are allowed.
- Negative integers are allowed.

## Value Validation

A value is invalid if:

- it is not an integer,
- it is a boolean value.

For invalid values, raise a `ValueError`.
