import math


def _validate_radius(
    radius: float,
) -> None:
    if not math.isfinite(
        radius,
    ):
        raise ValueError(
            "Radius must be a finite number."
        )

    if radius < 0:
        raise ValueError(
            "Radius must be non-negative."
        )


def circle_area(
    radius: float,
) -> float:
    _validate_radius(
        radius,
    )

    return math.pi * radius * radius


def circle_circumference(
    radius: float,
) -> float:
    _validate_radius(
        radius,
    )

    return 2 * math.pi * radius
