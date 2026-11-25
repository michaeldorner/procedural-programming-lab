# Lab 27: Checkout Simulator

**Topics:** Lists, nested loops, greedy selection, guard clauses  
**Lectures:** 08 (Loops), 09 (Built-in Collections), 10 (Collection Processing Patterns)

Simulate assigning incoming customers to the checkout lane with the shortest current wait time.

## Requirements

- Implement `simulate_checkout` to raise a value error if lane count is non-positive or any service duration is negative.
- Assign each customer in order to the lane with minimum accumulated load (breaking ties by lowest lane index) and return the final lane loads and total clearing time.

## Worked Examples

- Service times [5, 3, 2, 4] across 2 lanes yield ([9, 5], 9).

## Implementation Hints

- Track lane loads in a `list[int]` without mutating `customer_times`.
- Optional (for pros): Use [`min()`](https://docs.python.org/3/library/functions.html#min) on `range(num_lanes)` with `key=lanes.__getitem__`.

## Run & Test

```bash
python checkout_simulator.py
python -m unittest
```
