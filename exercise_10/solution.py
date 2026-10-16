import math


# Student template

def triangle_type(
    a: float,
    b: float,
    c: float,
) -> str:
    pass


# Basic solution

def triangle_type(
    a: float,
    b: float,
    c: float,
) -> str:
    if a == b == c:
        return "equilateral"

    if a == b or a == c or b == c:
        return "isosceles"

    return "scalene"


# Excellent solution for bonus tests

def _validate_side_length(
    value: float,
    name: str,
) -> None:
    if type(value) not in (
        int,
        float,
    ):
        raise ValueError(
            f"{name} must be a number."
        )

    if not math.isfinite(
        value,
    ):
        raise ValueError(
            f"{name} must be a finite number."
        )

    if value <= 0:
        raise ValueError(
            f"{name} must be greater than zero."
        )


def _is_valid_triangle(
    a: float,
    b: float,
    c: float,
) -> bool:
    return (
        a + b > c
        and a + c > b
        and b + c > a
    )


def triangle_type(
    a: float,
    b: float,
    c: float,
) -> str:
    _validate_side_length(
        a,
        "a",
    )

    _validate_side_length(
        b,
        "b",
    )

    _validate_side_length(
        c,
        "c",
    )

    if not _is_valid_triangle(
        a,
        b,
        c,
    ):
        return "invalid"

    if a == b == c:
        return "equilateral"

    if a == b or a == c or b == c:
        return "isosceles"

    return "scalene"
