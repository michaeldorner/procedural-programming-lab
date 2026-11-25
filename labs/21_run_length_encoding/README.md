# Lab 21: Run-Length Encoding

**Topics:** String parsing, loops, guard clauses, optional return values  
**Lectures:** 08 (Loops), 13 (Text Processing)

Compress runs of repeated non-digit characters into `<count><char>` pairs and decode them back safely.

## Requirements

- Implement `rle_encode` to reject inputs containing digits by returning no value, preserve empty text, and encode each consecutive run as its count followed by the character.
- Implement `rle_decode` to reconstruct the original text, returning no value if counts are missing, zero, or followed by no character.

## Worked Examples

- "AAABBC" encodes to "3A2B1C"; "0A" or "3A2" fails decoding.

## Implementation Hints

- See [`str.isdigit()`](https://docs.python.org/3/library/stdtypes.html#str.isdigit) and [`str.join()`](https://docs.python.org/3/library/stdtypes.html#str.join).

## Run & Test

```bash
python run_length_encoding.py
python -m unittest
```
