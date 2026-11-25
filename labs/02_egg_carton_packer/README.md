# Lab 02: Egg Carton Packer

**Topics:** Functions, integer division, modulo arithmetic  
**Lectures:** 02 (Data Types, Variables & Naming), 03 (Operators & Expressions), 04 (Functions)

Calculate how many full cartons, loose eggs, and total cartons are needed to pack a batch of eggs.

## Requirements

- Implement `count_full_cartons` to return $\lfloor \text{eggs} / \text{capacity} \rfloor$.
- Implement `count_loose_eggs` to return the remaining eggs $\text{eggs} \bmod \text{capacity}$.
- Implement `calculate_minimum_cartons` to return $\lceil \text{eggs} / \text{capacity} \rceil$ using integer arithmetic.
- Reject negative egg counts or non-positive carton capacities with a value error.

## Worked Examples

- 26 eggs with capacity 12 yields 2 full cartons, 2 loose eggs, and 3 cartons needed.
- 24 eggs with capacity 12 requires 2 cartons.

## Implementation Hints

- Use `//` and `%`; see [Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).
- Optional (for pros): Use [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) to compute quotient and remainder in one call.

## Run & Test

```bash
python egg_carton_packer.py
python -m unittest
```
