# Student template
def guess_feedback(
    secret: int,
    guess: int,
) -> str:
    pass


# Basic solution
def guess_feedback(
    secret: int,
    guess: int,
) -> str:
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"


# Excellent solution for bonus tests
def guess_feedback(
    secret: int,
    guess: int,
) -> str:
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"
