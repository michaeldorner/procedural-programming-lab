# Lab 13: Manhattan Distance

**Topics:** Functions, tuples, loops, input validation, exceptions  
**Lectures:** 04 (Functions), 07 (Validation & Exceptions), 08 (Loops), 09 (Built-in Collections)

Compute the $n$-dimensional Manhattan (taxicab) distance between two integer coordinate tuples.

## Requirements

- Implement `calculate_manhattan_distance` to compute the sum of absolute coordinate differences $\sum_{i=1}^{n} |a_i - b_i|$ between two equal-length coordinate tuples.
- Reject coordinate tuples of differing dimensions by raising a value error.

## Worked Examples

- `(1, 2)` to `(4, 6)` has distance `7`; `(-1, 0, 2)` to `(2, -3, 2)` has distance `6`.
- `(1, 2)` and `(1, 2, 3)` raises an error due to mismatched dimensions.

## Implementation Hints

- See [`abs()`](https://docs.python.org/3/library/functions.html#abs), and [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError). You might also want to have a look into [`zip()`](https://docs.python.org/3/library/functions.html#zip).
- Optional (for pros): Combine [`sum()`](https://docs.python.org/3/library/functions.html#sum) with a generator expression and [`zip(..., strict=True)`](https://docs.python.org/3/library/functions.html#zip).

## Run & Test

```bash
python manhattan_distance.py
python -m unittest
```
