# Lab 05: Leap Year

**Topics:** Functions, boolean expressions, modulo arithmetic  
**Lectures:** 03 (Operators & Expressions), 04 (Functions)

Determine whether a calendar year is a valid Gregorian leap year.

## Requirements

- Implement `is_leap_year` so non-positive years are rejected as not leap years.
- A positive year is a leap year if it is divisible by 400, or divisible by 4 and not divisible by 100.

## Worked Examples

- 2000 and 2024 are leap years; 1900, 2023, 0, and -4 are not.

## Implementation Hints

- Combine `%` with `and`/`or`; see [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not).

## Run & Test

```bash
python leap_year.py
python -m unittest
```
