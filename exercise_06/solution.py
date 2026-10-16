# Student template

def is_even(
    number: int,
) -> bool:
    pass


# Basic solution

def is_even(
    number: int,
) -> bool:
    return number % 2 == 0


# Excellent solution for bonus tests

def _validate_integer(
    number: int,
) -> None:
    if type(number) is not int:
        raise ValueError(
            "Number must be an integer."
        )


def is_even(
    number: int,
) -> bool:
    _validate_integer(
        number,
    )

    return number % 2 == 0
