# Lab 20: ISBN Validator

**Topics:** String normalization, loops, weighted checksums, boolean functions  
**Lectures:** 08 (Loops), 10 (Collection Processing Patterns), 13 (Text Processing)

Validate ISBN-10 and ISBN-13 book identifiers after stripping whitespace and hyphens.

## Requirements

- Implement `is_valid_isbn10` to verify 10 characters (first 9 digits, last digit or `X` for 10) satisfying $\sum_{i=1}^{10}(11-i)d_i \equiv 0 \pmod{11}$.
- Implement `is_valid_isbn13` to verify 13 digits satisfying $\sum_{i=0}^{12} w_i d_i \equiv 0 \pmod{10}$ with alternating weights $w_i \in \{1, 3\}$.

## Worked Examples

- "0-306-40615-2" and "978-0-306-40615-7" are both valid.

## Implementation Hints

- See [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) and [`str.replace()`](https://docs.python.org/3/library/stdtypes.html#str.replace).
- Optional (for pros): Use [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) with a generator expression inside [`sum()`](https://docs.python.org/3/library/functions.html#sum).

## Run & Test

```bash
python isbn_validator.py
python -m unittest
```
