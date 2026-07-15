import math


# Student template

def distance(
    point_a: tuple[float, float],
    point_b: tuple[float, float],
) -> float:
    pass


# Basic solution

def distance(
    point_a: tuple[float, float],
    point_b: tuple[float, float],
) -> float:
    x1, y1 = point_a
    x2, y2 = point_b

    return math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
    )


# Excellent solution for bonus tests

def _validate_point(
    point: tuple[float, float],
) -> None:
    if len(point) != 2:
        raise ValueError(
            "A point must contain exactly two coordinates."
        )

    x, y = point

    if not math.isfinite(x) or not math.isfinite(y):
        raise ValueError(
            "Point coordinates must be finite numbers."
        )


def distance(
    point_a: tuple[float, float],
    point_b: tuple[float, float],
) -> float:
    _validate_point(
        point_a,
    )

    _validate_point(
        point_b,
    )

    x1, y1 = point_a
    x2, y2 = point_b

    return math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
    )
