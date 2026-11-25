# Lab 10: Triangle Geometry

**Topics:** Helper decomposition, branching, guard clauses, standard library math  
**Lectures:** 04 (Functions), 06 (Branching)

Validate triangle side lengths, classify triangles by side equality, and compute area via Heron's formula.

## Requirements

- Implement `is_valid_triangle` to verify all sides are strictly positive and satisfy $a + b > c$, $a + c > b$, and $b + c > a$.
- Implement `classify_triangle` to return no value if invalid, or equilateral, isosceles, or scalene.
- Implement `triangle_area` to return $\sqrt{s(s - a)(s - b)(s - c)}$ with $s = \frac{a + b + c}{2}$, raising a value error if invalid.

## Worked Examples

- (3, 4, 5) is scalene with area 6.0; (1, 2, 3) is invalid.

## Implementation Hints

- Use [`math.sqrt()`](https://docs.python.org/3/library/math.html#math.sqrt) for the square root.

## Run & Test

```bash
python triangle_geometry.py
python -m unittest
```
