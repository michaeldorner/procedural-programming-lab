# Exercise 13: Multiplication Table

## Objective

Implement a function that creates a multiplication table for a given integer.

## Tasks

Implement the following function in `solution.py`:

```python
def multiplication_table(
    number: int,
    start: int,
    end: int,
) -> listpass
```

## Rule

The function should return a list containing the products of `number` multiplied by all integers from `start` to `end`.

The range is inclusive.

```text
number * start
number * (start + 1)
...
number * end
```

## Examples

```python
multiplication_table(
    3,
    1,
    10,
)
```

returns

```python
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

```python
multiplication_table(
    5,
    3,
    6,
)
```

returns

```python
[15, 20, 25, 30]
```

```python
multiplication_table(
    0,
    1,
    5,
)
```

returns

```python
[0, 0, 0, 0, 0]
```

## Notes

- Use a loop for the basic solution.
- Return a list of products.
- Do not print the multiplication table inside the function.
- Do not change the function signature.
- The range is inclusive.
- For this exercise, `start` must be less than or equal to `end`.

## Bonus

The excellent solution should also validate the input.

The values are invalid if:

- `number` is not an integer,
- `start` is not an integer,
- `end` is not an integer,
