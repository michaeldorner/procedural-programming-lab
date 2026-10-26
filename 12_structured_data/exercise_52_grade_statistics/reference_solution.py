def grade_statistics(
    grades: list[float],
) -> tuple[float, float, float]:
    return sum(grades) / len(grades), min(grades), max(grades)
