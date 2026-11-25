# Lab 18: Slug Normalizer

**Topics:** String methods, character filtering, loops  
**Lectures:** 08 (Loops), 13 (Text Processing)

Convert arbitrary title text into clean, lowercase ASCII URL slugs.

## Requirements

- Implement `normalize_slug` to convert text to lowercase, keep only ASCII letters and digits, and collapse runs of spaces, underscores, or punctuation into single hyphens.
- Ensure no leading or trailing hyphens remain, returning empty text when no alphanumeric characters are present.

## Worked Examples

- "  Hello, World!  2026 " becomes "hello-world-2026"; "___!!!" becomes "".

## Implementation Hints

- See [`str.isascii()`](https://docs.python.org/3/library/stdtypes.html#str.isascii), [`str.isalnum()`](https://docs.python.org/3/library/stdtypes.html#str.isalnum), and [`str.strip()`](https://docs.python.org/3/library/stdtypes.html#str.strip).

## Run & Test

```bash
python slug_normalizer.py
python -m unittest
```
