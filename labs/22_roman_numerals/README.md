# Lab 22: Roman Numerals

**Topics:** Lookup tables, loops, string building, dictionaries, round-trip validation  
**Lectures:** 08 (Loops), 09 (Built-in Collections), 13 (Text Processing)

Convert integers between 1 and 3999 to canonical Roman numerals and parse canonical Roman numerals back.

## Requirements

- Implement `int_to_roman` to reject integers outside $[1, 3999]$ and produce the canonical Roman numeral for valid integers.
- Implement `roman_to_int` to parse case-insensitive Roman numerals and reject invalid symbols or non-canonical forms (such as `IIII` or `IC`).

## Worked Examples

- 1994 converts to "MCMXCIV" and back; "IIII" is rejected.

## Implementation Hints

- Use an ordered table of `(value, symbol)` pairs and verify canonical form by round-tripping via `int_to_roman`.

## Run & Test

```bash
python roman_numerals.py
python -m unittest
```
