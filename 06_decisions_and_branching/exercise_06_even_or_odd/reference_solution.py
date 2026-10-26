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
