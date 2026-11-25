"""Lab 10: Triangle Geometry."""

import math


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Return True if positive sides a, b, c satisfy the triangle inequality."""
    if a <= 0.0 or b <= 0.0 or c <= 0.0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)


def classify_triangle(a: float, b: float, c: float) -> str:
    """Classify a valid triangle as 'equilateral', 'isosceles', or 'scalene'.

    Raises:
        ValueError: If side lengths are non-positive or violate the triangle inequality.
    """
    if not is_valid_triangle(a, b, c):
        raise ValueError(f"Invalid triangle side lengths: ({a}, {b}, {c})")
    if math.isclose(a, b) and math.isclose(b, c):
        return "equilateral"
    if math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
        return "isosceles"
    return "scalene"


def triangle_area(a: float, b: float, c: float) -> float:
    """Return Heron's area for a valid triangle.

    Raises:
        ValueError: If side lengths are non-positive or violate the triangle inequality.
    """
    if not is_valid_triangle(a, b, c):
        raise ValueError(f"Invalid triangle side lengths: ({a}, {b}, {c})")
    s: float = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    print(classify_triangle(3.0, 4.0, 5.0), triangle_area(3.0, 4.0, 5.0))
