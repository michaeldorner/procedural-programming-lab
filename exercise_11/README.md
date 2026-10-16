# Exercise 11: Sum Between

## Objective

Implement a function that calculates the sum of all integers between two given values.

## Tasks

Implement the following function in `solution.py`:

```python
def sum_between(
    start: int,
    end: int,
) -> int:
    pass
```

## Rule

The function should calculate the inclusive sum from `start` to `end`.

This means both boundary values are included.

```text
start + (start + 1) + ... + end
```

For example:

```text
sum_between(1, 5) = 1 + 2 + 3 + 4 + 5 = 15
```

```text
sum_between(3, 6) = 3 + 4 + 5 + 6 = 18
```

## Examples

```python
sum_between(
    1,
    5,
)
```

returns

```python
15
```

```python
sum_between(
    3,
    6,
)
```

returns

```python
18
```

```python
sum_between(
    5,
    5,
)
```

returns

```python
5
```

## Notes

- Return the calculated sum.
- Do not print the result inside the function.
- Do not change the function signature.

## Bonus

The excellent solution should also validate the input.

For invalid values, raise a `ValueError`.
