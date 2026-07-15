# Student template

def rectangle_area(
    width: float,
    height: float,
) -> float:  # type: ignore
    pass


def rectangle_perimeter(
    width: float,
    height: float,
) -> float:  # type: ignore
    pass


# Basic solution

def rectangle_area(  # type: ignore
    width: float,
    height: float,
) -> float:
    return width * height


def rectangle_perimeter(  # type: ignore
    width: float,
    height: float,
) -> float:
    return 2 * (width + height)


# Excellent solution for bonus tests

def rectangle_area(  # type: ignore
    width: float,
    height: float,
) -> float:
    if width < 0 or height < 0:
        raise ValueError(
            "Width and height must be non-negative."
        )

    return width * height


def rectangle_perimeter(  # type: ignore
    width: float,
    height: float,
) -> float:
    if width < 0 or height < 0:
        raise ValueError(
            "Width and height must be non-negative."
        )

    return 2 * (width + height)
