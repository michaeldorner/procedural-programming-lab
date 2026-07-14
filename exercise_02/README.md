# Exercise 02: Temperature Conversion

## Objective

Implement two functions that convert temperatures between Celsius and Fahrenheit.

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

## Formulas

### Celsius to Fahrenheit

```text
F = C × 9 / 5 + 32
```

### Fahrenheit to Celsius

```text
C = (F - 32) × 5 / 9
```

## Examples

### Celsius to Fahrenheit

```python
celsius_to_fahrenheit(0.0)
```

returns

```python
32.0
```

### Fahrenheit to Celsius

```python
fahrenheit_to_celsius(212.0)
```

returns

```python
100.0
```

## Required Tests

Run the required tests:

```bash
python -m unittest discover tests/required -v
```

## Bonus Tests

Run the bonus tests:

```bash
python -m unittest discover tests/bonus -v
```

## Run All Tests

```bash
python -m unittest discover tests -v
```

## Coding Guidelines

- Follow PEP 8.
- Do not modify the tests.
- Do not change the function signatures.
- Use type hints.


## Expected Results

### Passed

```text
✅ exercise_02
```

### Passed with Distinction

```text
🌟 exercise_02
```
