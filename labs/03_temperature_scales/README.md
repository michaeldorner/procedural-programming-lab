# Lab 03: Temperature Scales

**Topics:** Floating-point arithmetic, operator precedence, input validation, exceptions  
**Lectures:** 02 (Data Types, Variables & Naming), 03 (Operators & Expressions), 04 (Functions), 07 (Validation & Exceptions)

Convert temperatures between Celsius ($C$), Fahrenheit ($F$), and Kelvin ($K$) while enforcing physical absolute-zero bounds.

## Requirements

- Implement `convert_celsius_to_fahrenheit` using $F = \frac{9}{5}C + 32$.
- Implement `convert_fahrenheit_to_celsius` using $C = \frac{5}{9}(F - 32)$.
- Implement `convert_celsius_to_kelvin` using $K = C + 273.15$.
- Reject non-finite values and temperatures strictly below absolute zero ($-273.15\,^\circ{C}$ or $-459.67\,^\circ{F}$) with a value error, while allowing exact absolute zero.

## Worked Examples

- `0.0 °C` becomes `32.0 °F`; `212.0 °F` becomes `100.0 °C`; `-273.15 °C` becomes `0.0 K`.
- `-274.0 °C` or `-460.0 °F` raises an error.

## Implementation Hints

See [Floating-Point Arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html), [`math.isfinite()`](https://docs.python.org/3/library/math.html#math.isfinite), and [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError).

## Run & Test

```bash
python temperature_scales.py
python -m unittest
```
