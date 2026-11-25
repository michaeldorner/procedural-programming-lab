# Lab 09: ATM Dispenser

**Topics:** Functions, guard clauses, exceptions, integer division, modulo arithmetic, tuples  
**Lectures:** 03 (Operators & Expressions), 06 (Branching), 07 (Validation & Exceptions), 09 (Built-in Collections)

Break down an ATM withdrawal into 100, 50, 20, and 10 EUR banknotes while separating invalid arguments from declined transactions.

## Requirements

- Implement `dispense_banknotes` to raise a value error for invalid arguments: non-positive withdrawal amount, negative account balance, or amount not divisible by 10.
- For valid requests that exceed the available account balance (insufficient funds), decline the transaction by returning no value.
- For approved withdrawals, return the 4-part counts of 100, 50, 20, and 10 EUR notes greedily from largest to smallest.

## Worked Examples

- `180 EUR` with `500 EUR` balance returns `(1, 1, 1, 1)`.
- `200 EUR` with `100 EUR` balance returns no value (declined).
- `55 EUR` or `-20 EUR` raises an error (invalid argument).

## Implementation Hints

- Use `//` and `%` to peel off each denomination into a `tuple[int, int, int, int] | None`, and raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) for invalid arguments.
- Optional (for pros): Use [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) in a loop over `(100, 50, 20, 10)`.

## Run & Test

```bash
python atm_dispenser.py
python -m unittest
```
