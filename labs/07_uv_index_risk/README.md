# Lab 07: UV Index Risk

**Topics:** Functions, branching, boundary checks, input validation, exceptions  
**Lectures:** 04 (Functions), 06 (Branching)

Classify a UV index reading into WHO risk brackets and decide whether sun protection is needed.

## Requirements

- Implement `classify_uv_risk` to reject negative or non-finite values with a value error, and otherwise classify into low (below 3), moderate (3 to under 6), high (6 to under 8), very high (8 to under 11), or extreme (11 and above).
- Implement `needs_sun_protection` to indicate yes whenever the UV index is at least 3.0.

## Worked Examples

- -0.5 raises an error; 2.9 is low (no protection); 3.0 is moderate (protection needed).

## Implementation Hints

- See [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) and [`math.isfinite()`](https://docs.python.org/3/library/math.html#math.isfinite). You can also store the thresholds in a tuple of `(upper_bound, label)` pairs and iterate over it.
- Optional (for pros): Store `(upper_bound, label)` pairs in a tuple and iterate over it instead of a long `elif` chain.

## Run & Test

```bash
python uv_index_risk.py
python -m unittest
```
