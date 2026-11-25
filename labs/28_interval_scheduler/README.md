# Lab 28: Interval Scheduler

**Topics:** Lists of tuples, sorting with key functions, greedy loops, non-mutation  
**Lectures:** 09 (Built-in Collections), 10 (Collection Processing Patterns)

Select the maximum set of non-overlapping meetings from `(start, end)` intervals.

## Requirements

- Implement `select_max_meetings` to raise a value error if any interval has start greater than or equal to end.
- Select non-overlapping intervals greedily by earliest finish time (allowing touching endpoints) without mutating the input list.

## Worked Examples

- [(1, 4), (3, 5), (0, 6), (4, 7)] selects [(1, 4), (4, 7)].

## Implementation Hints

- Use [`sorted(..., key=...)`](https://docs.python.org/3/library/functions.html#sorted) to avoid mutating `intervals`.

## Run & Test

```bash
python interval_scheduler.py
python -m unittest
```
