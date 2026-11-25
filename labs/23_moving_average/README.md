# Lab 23: Moving Average

**Topics:** Lists, list slicing, loops, guard clauses  
**Lectures:** 08 (Loops), 09 (Built-in Collections), 10 (Collection Processing Patterns)

Compute the Simple Moving Average (SMA) over a fixed window without modifying the input series.

## Requirements

- Implement `calculate_moving_average` to raise a value error when the window size is non-positive, and an empty list when the series is shorter than the window.
- Otherwise return the arithmetic mean of every contiguous slice of length `window`.

## Worked Examples

- [1.0, 2.0, 3.0, 4.0] with window 2 yields [1.5, 2.5, 3.5].

## Implementation Hints

- Use list slicing `values[i : i + window]` and [`sum()`](https://docs.python.org/3/library/functions.html#sum).
- Optional (for pros): Use a list comprehension over `range(len(values) - window + 1)`.

## Run & Test

```bash
python moving_average.py
python -m unittest
```
