# Exercise 08: Leap Year

## Objective

Implement a function that determines whether a year is a leap year.

## Tasks

Implement the following function in `solution.py`:

```python
def is_leap_year(
    year: int,
) -> bool:
    pass
```

## Leap Year Rule

A year is a leap year if it is divisible by `4`.

However, there is an additional rule for full centuries:

- A year divisible by `100` is not a leap year,
- unless it is also divisible by `400`.

## Examples

```python
is_leap_year(
    2024,
)
```

returns

```python
True
```

```python
is_leap_year(
    2023,
)
```

returns

```python
False
```

```python
is_leap_year(
    2000,
)
```

returns

```python
True
```

```python
is_leap_year(
    1900,
)
```

returns

```python
False
```

## Notes

- Return `True` if the year is a leap year.
- Return `False` otherwise.
- For this exercise, valid calendar years start at `1`.
- Do not print the result inside the function.
- Do not change the function signature.

## Year Validation

A year is invalid if:

- it is not an integer,
- it is a boolean value,
- it is less than `1`.

For invalid years, raise a `ValueError`.
