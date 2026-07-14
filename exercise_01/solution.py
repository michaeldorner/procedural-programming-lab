def rectangle_area(
    width: float,
    height: float,
) -> float:  # type: ignore

    if width < 0 or height < 0:
        raise ValueError(
            "Dimensions must be non-negative."
        )

    return width * height


def rectangle_perimeter(
    width: float,
    height: float,
) -> float:  # type: ignore

    if width < 0 or height < 0:
        raise ValueError(
            "Dimensions must be non-negative."
        )

    return 2 * width + 2 * height


if __name__ == "__main__":
    assert rectangle_area(3.0, 4.0) == 12.0
    assert rectangle_perimeter(3.0, 4.0) == 14.0
