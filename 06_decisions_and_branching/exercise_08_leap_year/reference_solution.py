def _validate_year(
    year: int,
) -> None:
    if type(year) is not int:
        raise ValueError(
            "Year must be an integer."
        )

    if year <= 0:
        raise ValueError(
            "Year must be greater than zero."
        )


def is_leap_year(
    year: int,
) -> bool:
    _validate_year(
        year,
    )

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0
