def _validate_integer(
    value: int,
    name: str,
) -> None:
    if type(value) is not int:
        raise ValueError(
            f"{name} must be an integer."
        )


def minimum_of_three(
    a: int,
    b: int,
    c: int,
) -> int:
    _validate_integer(
        a,
        "a",
    )

    _validate_integer(
        b,
        "b",
    )

    _validate_integer(
        c,
        "c",
    )

    minimum = a

    if b < minimum:
        minimum = b

    if c < minimum:
        minimum = c

    return minimum
