# Exercise 07: Grade Classification

## Objective

Implement a function that converts a numeric score into a letter grade.

## Tasks

Implement the following function in `solution.py`:

```python
def grade(
    score: int,
) -> str:
    pass
```

## Grade Scale

Use the following grade scale:

```text
90 - 100    A
80 - 89     B
70 - 79     C
60 - 69     D
0  - 59     F
```

## Examples

```python
grade(
    95,
)
```

returns

```python
"A"
```

```python
grade(
    82,
)
```

returns

```python
"B"
```

```python
grade(
    58,
)
```

returns

```python
"F"
```

## Notes

- Return the letter grade as a string.
- Do not print the result inside the function.
- Do not change the function signature.

## Bonus

The excellent solution should also validate the input.

A score is invalid if:

- it is less than `0`,
- it is greater than `100`,
- it is not an integer,
- it is a boolean value.

For invalid scores, raise a `ValueError`.
