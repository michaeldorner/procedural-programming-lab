# Student template

def sum_between(
    start: int,
    end: int,
) -> int:
    pass


# Basic solution

def sum_between(
    start: int,
    end: int,
) -> int:
    total = 0

    for number in range(
        start,
        end + 1,
    ):
        total = total + number

    return total


# Excellent solution for bonus tests

def _validate_integer(
    value: int,
    name: str,
) -> None:
    if type(value) is not int:
        raise ValueError(
            f"{name} must be an integer."
        )


def sum_between(
    start: int,
    end: int,
) -> int:
    _validate_integer(
        start,
        "start",
    )

    _validate_integer(
        end,
        "end",
    )

    if start > end:
        raise ValueError(
            "start must be less than or equal to end."
        )

    return sum(
        range(
            start,
            end + 1,
        )
    )
