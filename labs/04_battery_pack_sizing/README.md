# Lab 04: Battery Pack Sizing

**Topics:** Functions, integer and floating-point arithmetic  
**Lectures:** 02 (Data Types, Variables & Naming), 03 (Operators & Expressions), 04 (Functions)

Compute pack voltage, total Watt-hour energy capacity, and estimated charging duration for a battery array.

## Requirements

- Implement `pack_voltage` as the product of cell voltage and series cell count.
- Implement `pack_energy_wh` as the product of cell voltage, cell capacity in Ah, series count, and parallel count.
- Implement `charge_time_hours` as $\frac{\text{energy\_wh}}{\text{charger\_watts} \cdot \text{efficiency}}$.
- Reject non-positive cell ratings, cell counts, or charger power, negative energy, or efficiency outside $(0, 1]$ with a value error.

## Worked Examples

- 10 cells at 3.6 V in series give 36.0 V; 4 parallel strings of 2.5 Ah cells store 360.0 Wh.
- Charging 360.0 Wh at 100.0 W and 90% efficiency takes 4.0 hours.

## Implementation Hints

- Use parentheses around the denominator product; see [Expressions](https://docs.python.org/3/reference/expressions.html).

## Run & Test

```bash
python battery_pack_sizing.py
python -m unittest
```
