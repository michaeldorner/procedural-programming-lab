# Lab 25: Resistor Networks

**Topics:** Lists, guard clauses, standard library math, key-based selection  
**Lectures:** 09 (Built-in Collections), 10 (Collection Processing Patterns)

Compute equivalent series and parallel resistances and find the closest standard E12 resistor value.

## Requirements

- Implement `calculate_series_resistance` ($\sum R_i$) and `calculate_parallel_resistance` ($(\sum \frac{1}{R_i})^{-1}$), raising a value error for empty lists or non-positive resistances.
- Implement `find_nearest_e12_value` to return the closest standard E12 decade value for positive target ohms, raising a value error otherwise.

## Worked Examples

- Parallel [100.0, 100.0] gives 50.0 ohms; nearest E12 to 460.0 is 470.0.

## Implementation Hints

- Use [`math.log10()`](https://docs.python.org/3/library/math.html#math.log10) and [`min(..., key=...)`](https://docs.python.org/3/library/functions.html#min).

## Run & Test

```bash
python resistor_networks.py
python -m unittest
```
