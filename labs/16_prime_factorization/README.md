# Lab 16: Prime Factorization

**Topics:** Nested `while` loops, guard clauses, lists  
**Lectures:** 06 (Branching), 08 (Loops), 09 (Built-in Collections)

Decompose integers into ascending prime factors and test primality.

## Requirements

- Implement `prime_factors` to raise a value error for integers below 2, and otherwise return all prime factors in ascending order.
- Implement `is_prime` to indicate whether an integer is at least 2 and has no divisors other than 1 and itself.

## Worked Examples

- 84 decomposes into [2, 2, 3, 7]; 29 is prime; 1 raises an error.

## Implementation Hints

- Test trial divisors up to $\lfloor \sqrt{n} \rfloor$ in a `while` loop and append any remaining factor $> 1$.

## Run & Test

```bash
python prime_factorization.py
python -m unittest
```
