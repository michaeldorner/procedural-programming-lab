def midpoint(
    point_a: tuple[float,
    float],
    point_b: tuple[float,
    float],
) -> tuple[float, float]:
    x1, y1 = point_a
    x2, y2 = point_b
    return ((x1 + x2) / 2, (y1 + y2) / 2)
