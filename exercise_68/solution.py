# Student template
def quiz_score(
    answers: list[str],
    correct_answers: list[str],
) -> int:
    pass


# Basic solution
def quiz_score(
    answers: list[str],
    correct_answers: list[str],
) -> int:
    score = 0
    for answer, correct_answer in zip(answers, correct_answers):
        if answer == correct_answer:
            score += 1
    return score


# Excellent solution for bonus tests
def quiz_score(
    answers: list[str],
    correct_answers: list[str],
) -> int:
    score = 0
    for answer, correct_answer in zip(answers, correct_answers):
        if answer == correct_answer:
            score += 1
    return score
