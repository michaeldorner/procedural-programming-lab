def guess_feedback(
    secret: int,
    guess: int,
) -> str:
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"
