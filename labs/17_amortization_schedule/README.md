# Lab 17: Amortization Schedule

**Topics:** Loops, guard clauses, lists of tuples, rounding  
**Lectures:** 06 (Branching), 08 (Loops), 09 (Built-in Collections)

Compute fixed monthly loan payments and a month-by-month principal/interest amortization schedule.

## Requirements

- Implement `calculate_monthly_payment` to raise a value error for non-positive principal/months or negative interest rate; handle zero-interest loans as equal principal installments and positive-rate loans via $M = P \frac{r(1+r)^n}{(1+r)^n - 1}$ with $r = \text{annual\_rate}/12$.
- Implement `build_amortization_schedule` to return a list of `(month, principal_paid, interest_paid, remaining_balance)` rows rounded to 2 decimal places with a non-negative final balance.

## Worked Examples

- 1200.0 EUR at 0% over 2 months yields [(1, 600.0, 0.0, 600.0), (2, 600.0, 0.0, 0.0)].

## Implementation Hints

- Clamp remaining balance with [`max()`](https://docs.python.org/3/library/functions.html#max) so rounding never produces `-0.0`.

## Run & Test

```bash
python build_amortization_schedule.py
python -m unittest
```
