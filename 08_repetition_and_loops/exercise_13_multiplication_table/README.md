# Exercise 13: Multiplication Table

## Objective

Implement a function that creates a multiplication table for a given integer from 1 to 10.

## Tasks

Implement the following function in `solution.py`:

```python
def multiplication_table(
    number: int,
) -> list[int]:
    pass
```

## Rule

The function should return a list containing the products of `number` multiplied by integers from 1 to 10.

## Examples

```python
multiplication_table(
    3,
)
```

returns

```python
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

```python
multiplication_table(
    0,
)
```

returns

```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Notes

- Return a list of products.
- Do not print the multiplication table inside the function.
- Do not change the function signature.
