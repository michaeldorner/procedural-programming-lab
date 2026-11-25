# Lab 08: Water Boiling Point

**Topics:** Functions, branching, guard clauses, optional return values  
**Lectures:** 04 (Functions), 06 (Branching)

Estimate the boiling point of water in Celsius from altitude in meters.

## Requirements

- Implement `estimate_boiling_point_c` to reject altitudes below -500 m or above 9000 m by raising a value error.
- Within the valid range, return $100.0 - 0.0033 \cdot \text{altitude\_m}$.

## Worked Examples

- 0 m yields 100.0 °C; 3000 m yields 90.1 °C; -600 m raises an error.

## Implementation Hints

- Return `None` in an early guard clause; see [Constants (`None`)](https://docs.python.org/3/library/constants.html#None).

## Run & Test

```bash
python water_boiling_point.py
python -m unittest
```
