# Exercise 72: Simple Image Data

## Objective

Calculate basic statistics from a plain-text PPM image file.

## Tasks

Implement the following functions in `solution.py`:

```python
def _read_pixel_brightness_values(
    filename: str,
) -> list[float]:
    pass

def average_brightness(
    filename: str,
) -> float:
    pass

def count_dark_pixels(
    filename: str,
    threshold: float,
) -> int:
    pass
```

## Examples

```python
average_brightness('data/simple_image.ppm')
```

returns

```python
0.5
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
