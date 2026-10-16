# Student template
def grade_statistics(
    grades: list[float],
) -> tuple[float, float, float]:
    pass


# Basic solution
def grade_statistics(
    grades: list[float],
) -> tuple[float, float, float]:
    return sum(grades) / len(grades), min(grades), max(grades)


# Excellent solution for bonus tests
def grade_statistics(
    grades: list[float],
) -> tuple[float, float, float]:
    return sum(grades) / len(grades), min(grades), max(grades)
