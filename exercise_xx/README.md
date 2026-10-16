# Exercise 05: ISBN-10 Validation

## Objective

Implement a function that checks whether a string is a valid ISBN-10 number.

## Tasks

Implement the following function in `solution.py`:

```python
def is_valid_isbn10(
    isbn: str,
) -> bool:
    pass
```

## ISBN-10 Check

An ISBN-10 consists of 10 characters.

For the required tests, all characters are digits.

To validate an ISBN-10, multiply each digit by a weight:

```text
10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

Then add the products.

The ISBN-10 is valid if the sum is divisible by `11`.

## Example

```python
is_valid_isbn10(
    "0306406152",
)
```

returns

```python
True
```

```python
is_valid_isbn10(
    "0306406153",
)
```

returns

```python
False
```

## Notes

- Return `True` if the ISBN-10 is valid.
- Return `False` if the ISBN-10 is invalid.
- Do not print the result inside the function.
- Do not change the function signature.

## Bonus

The excellent solution should also handle formatted ISBN-10 strings.

It should ignore:

- hyphens
- spaces

It should also support `X` as the final check digit.

The character `X` represents the value `10`.

Lowercase `x` should also be accepted.

Invalid input should return `False`.
