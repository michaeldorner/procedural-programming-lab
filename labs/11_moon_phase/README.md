# Lab 11: Moon Phase

**Topics:** Constants, modulo arithmetic, multi-way branching  
**Lectures:** 03 (Operators & Expressions), 05 (Scope), 06 (Branching)

Calculate synodic lunar age in days and classify it into the 8 standard lunar phases.

## Requirements

- Implement `calculate_lunar_age_days` to wrap the day offset into $[0, 29.530588)$.
- Implement `classify_moon_phase` to map the wrapped lunar age into 8 equal octants: new moon, waxing crescent, first quarter, waxing gibbous, full moon, waning gibbous, last quarter, or waning crescent.

## Worked Examples

- Day 0 is new moon (age 0.0); age 14.8 is full moon.

## Implementation Hints

- Use `% SYNODIC_MONTH_DAYS` for wrap-around across negative or large offsets.
- Optional (for pros): Index an 8-element tuple of phase names using `int(normalized // (SYNODIC_MONTH_DAYS / 8))`.

## Run & Test

```bash
python moon_phase.py
python -m unittest
```
