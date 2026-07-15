# Exercise 02: Temperature Conversion

## Objective

Convert temperatures between Celsius and Fahrenheit.

## Tasks

Implement the following functions in `solution.py`:

```python
def celsius_to_fahrenheit(
    celsius: float,
) -> float:
    pass

def fahrenheit_to_celsius(
    fahrenheit: float,
) -> float:
    pass
```

## Examples

```python
celsius_to_fahrenheit(0.0)
```

returns

```python
32.0
```
```python
fahrenheit_to_celsius(212.0)
```

returns

```python
100.0
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.

## Bonus

Negative temperatures are valid.

However, temperatures below absolute zero are not physically meaningful:

- below `-273.15 °C`
- below `-459.67 °F`

The excellent solution should raise a `ValueError` for such values.

The excellent solution should also reject non-finite values such as:

- `float("nan")`
- `float("inf")`
- `float("-inf")`

Roundtrip conversions should preserve the original value approximately:

```python
celsius -> fahrenheit -> celsius
fahrenheit -> celsius -> fahrenheit
