# Lab 15: Compound Interest

**Topics:** `for` and `while` loops, guard clauses, lists  
**Lectures:** 06 (Branching), 08 (Loops), 09 (Built-in Collections)

Simulate annual compound interest year by year and determine how many years are needed to reach a savings target.

## Requirements

- Implement `yearly_balances` to raise a value error for negative principal, rate, or years, and otherwise return balances from year 0 through year N rounded to 2 decimal places.
- Implement `years_to_target` to return the minimum whole years for a positive principal to reach at least the target, rejecting impossible inputs (such as non-positive rate when below target).

## Worked Examples

- 1000.0 EUR at 5% for 2 years gives [1000.0, 1050.0, 1102.5].
- 1000.0 EUR at 10% reaches 1200.0 EUR in 2 years.

## Implementation Hints

- Use [`round()`](https://docs.python.org/3/library/functions.html#round) for each yearly balance and a `while` loop for `years_to_target`.

## Run & Test

```bash
python compound_interest.py
python -m unittest
```
