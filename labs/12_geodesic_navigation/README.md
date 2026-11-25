# Lab 12: Geodesic Navigation

**Topics:** Functions, tuples, helper decomposition, input validation, standard library math  
**Lectures:** 04 (Functions), 05 (Scope), 07 (Validation & Exceptions), 09 (Built-in Collections)

Compute the Haversine great-circle distance between two `(latitude, longitude)` coordinate pairs on Earth ($R = 6371.0\text{ km}$).

## Requirements

- Implement `calculate_haversine_distance_km` taking two `(latitude, longitude)` pairs in degrees and returning the great-circle distance $d$ in kilometers:

$$a = \sin^2\left(\frac{\Delta\varphi}{2}\right) + \cos(\varphi_1)\cos(\varphi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right), \qquad d = 2 R \operatorname{atan2}\left(\sqrt{a}, \sqrt{1 - a}\right)$$

- Reject invalid coordinates with a value error if latitude is outside $[-90.0, 90.0]$ or longitude is outside $[-180.0, 180.0]$.

## Worked Examples

- Chemnitz `(50.8278, 12.9214)` to Berlin `(52.5200, 13.4050)` is approximately `191.09 km`.
- Latitude `95.0` or longitude `-185.0` raises an error.

## Implementation Hints

- [`math.radians()`](https://docs.python.org/3/library/math.html#math.radians)
- [`math.sin()`](https://docs.python.org/3/library/math.html#math.sin)
- [`math.cos()`](https://docs.python.org/3/library/math.html#math.cos)
- [`math.atan2()`](https://docs.python.org/3/library/math.html#math.atan2)
- [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError).

## Run & Test

```bash
python geodesic_navigation.py
python -m unittest
```
