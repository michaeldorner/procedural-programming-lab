# Lab 32: Matrix Algebra

**Topics:** 2D nested lists, helper functions, guard clauses, non-mutation  
**Lectures:** 08 (Loops), 09 (Built-in Collections), 11 (Mutability & Memory)

Implement pure 2D matrix addition, scalar multiplication, transposition, and matrix multiplication.

## Requirements

- Implement `add_matrices`, `scale_matrix`, `transpose_matrix`, and `multiply_matrices`.
- Raise a value error whenever any matrix is empty, has empty or unequal-length rows, or has incompatible dimensions for the operation.

## Worked Examples

- Multiplying [[1, 2], [3, 4]] by [[2, 0], [1, 2]] gives [[4, 4], [10, 8]].

## Implementation Hints

- Extract a shared helper to validate rectangular shapes and return `(rows, cols)`.
- Optional (for pros): Use nested list comprehensions with [`zip()`](https://docs.python.org/3/library/functions.html#zip) for `transpose_matrix`.

## Run & Test

```bash
python matrix_algebra.py
python -m unittest
```
