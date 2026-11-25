# Lab 19: Caesar Cipher

**Topics:** Character code arithmetic, modulo arithmetic, loops, string building  
**Lectures:** 08 (Loops), 13 (Text Processing)

Encrypt and decrypt ASCII alphabetic text using a Caesar shift while preserving case and punctuation.

## Requirements

- Implement `encrypt_caesar` to shift uppercase and lowercase ASCII letters forward by the given shift, wrapping around the 26-letter alphabet.
- Leave digits, spaces, and punctuation unchanged, and implement `decrypt_caesar` to reverse the shift.

## Worked Examples

- "Hello, World! 123" shifted by 3 becomes "Khoor, Zruog! 123".

## Implementation Hints

- Use [`ord()`](https://docs.python.org/3/library/functions.html#ord) and [`chr()`](https://docs.python.org/3/library/functions.html#chr) with `% 26`.
- Optional (for pros): Build a translation table with [`str.maketrans()`](https://docs.python.org/3/library/stdtypes.html#str.maketrans) and [`str.translate()`](https://docs.python.org/3/library/stdtypes.html#str.translate).

## Run & Test

```bash
python caesar_cipher.py
python -m unittest
```
