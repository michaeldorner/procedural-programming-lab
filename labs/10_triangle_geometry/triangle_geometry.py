"""Lab 10: Triangle Geometry."""


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Return True if positive sides a, b, c satisfy the triangle inequality."""
    raise NotImplementedError


def classify_triangle(a: float, b: float, c: float) -> str:
    """Classify a valid triangle as 'equilateral', 'isosceles', or 'scalene'.

Raises:
    ValueError: If side lengths are non-positive or violate the triangle inequality.
    """
    raise NotImplementedError


def calculate_triangle_area(a: float, b: float, c: float) -> float:
    """Return Heron's area for a valid triangle.

Raises:
    ValueError: If side lengths are non-positive or violate the triangle inequality.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(classify_triangle(3.0, 4.0, 5.0), calculate_triangle_area(3.0, 4.0, 5.0))
