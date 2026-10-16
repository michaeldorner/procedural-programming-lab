import math


# Student template

def factorial(
    n: int,
) -> int:
    pass


# Basic solution

def factorial(
    n: int,
) -> int:
    result = 1

    for number in range(
        2,
        n + 1,
    ):
        result = result * number

    return result


# Excellent solution for bonus tests

def _validate_n(
    n: int,
) -> None:
    if type(n) is not int:
        raise ValueError(
            "n must be an integer."
        )

    if n < 0:
        raise ValueError(
            "n must be greater than or equal to zero."
        )


def factorial(
    n: int,
) -> int:
    _validate_n(
        n,
    )

    return math.factorial(
        n,
    )
