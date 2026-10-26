def calculate_rectangle_area(
    width: float,
    height: float,
) -> float:
    if width < 0 or height < 0:
        raise ValueError(
            "Width and height must be non-negative."
        )

    return width * height


def calculate_rectangle_perimeter(
    width: float,
    height: float,
) -> float:
    if width < 0 or height < 0:
        raise ValueError(
            "Width and height must be non-negative."
        )

    return 2 * (width + height)
