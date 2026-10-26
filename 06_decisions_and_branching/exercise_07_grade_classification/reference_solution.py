def _validate_score(
    score: int,
) -> None:
    if type(score) is not int:
        raise ValueError(
            "Score must be an integer."
        )

    if score < 0 or score > 100:
        raise ValueError(
            "Score must be between 0 and 100."
        )


def grade(
    score: int,
) -> str:
    _validate_score(
        score,
    )

    if score >= 90:
        return "A"

    if score >= 80:
        return "B"

    if score >= 70:
        return "C"

    if score >= 60:
        return "D"

    return "F"
