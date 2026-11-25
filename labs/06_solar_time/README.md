# Lab 06: Solar Time

**Topics:** Functions, floating-point arithmetic, modulo wrap-around  
**Lectures:** 03 (Operators & Expressions), 04 (Functions)

Calculate apparent solar time from standard clock hours, longitude offset, and the equation of time.

## Requirements

- Implement `calculate_solar_noon_offset_minutes` as $4 \cdot (\text{meridian\_deg} - \text{longitude\_deg}) - \text{equation\_of\_time\_min}$.
- Implement `calculate_apparent_solar_hour` by shifting standard clock hours by the negative offset in hours and wrapping into $[0, 24)$.
- Reject non-finite inputs or longitudes/meridians outside $[-180^\circ, 180^\circ]$ with a value error.

## Worked Examples

- At longitude 12.92° with meridian 15.0° and 0.0 EoT, the offset is 8.32 minutes.
- Shifting 0.1 h back by 1.0 h wraps around to 23.1 h.

## Implementation Hints

- Use `% 24.0` for 24-hour wrap-around; see [Binary Arithmetic Operations](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations).

## Run & Test

```bash
python solar_time.py
python -m unittest
```
