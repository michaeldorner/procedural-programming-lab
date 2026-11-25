# Lab 14: Collatz Conjecture

**Topics:** Indeterminate `while` loops, guard clauses, lists  
**Lectures:** 06 (Branching), 08 (Loops), 09 (Built-in Collections)

Generate Collatz sequences, count stopping times, and find peak values for positive integers.

## Requirements

- Implement `generate_collatz_sequence`, `count_collatz_steps`, and `find_collatz_peak` to raise a value error for non-positive starting integers.
- Repeatedly halve even numbers and map odd numbers $n$ to $3n + 1$ until reaching $1$.

## Worked Examples

- Starting at 6 produces [6, 3, 10, 5, 16, 8, 4, 2, 1] with 8 steps and peak 16.

## Implementation Hints

- Use a [`while` loop](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) and [`max()`](https://docs.python.org/3/library/functions.html#max) on the generated list.

## Run & Test

```bash
python collatz_conjecture.py
python -m unittest
```
