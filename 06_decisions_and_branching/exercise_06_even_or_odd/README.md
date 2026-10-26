# Exercise 06: Even or Odd

## Objective

Implement a function that determines whether an integer is even.

## Tasks

Implement the following function in `solution.py`:

```python
def is_even(
    number: int,
) -> bool:
    pass
```

## Rule

An integer is even if it is divisible by `2`.

In Python, the modulo operator `%` gives the remainder of a division.

```python
number % 2
```

If the remainder is `0`, the number is even.

## Examples

```python
is_even(
    4,
)
```

returns

```python
True
```

```python
is_even(
    5,
)
```

returns

```python
False
```

## Notes

- Return `True` if the number is even.
- Return `False` if the number is odd.
- `0` is even.
- Negative integers can also be even or odd.
- Do not print the result inside the function.
- Do not change the function signature.

## Input Validation

The function should raise a `ValueError` if the input is not an integer.

This includes values such as:

- `True`
- `False`
- `2.0`

Even though `True` and `False` behave like numbers in some Python expressions, they should not be accepted in this exercise.
