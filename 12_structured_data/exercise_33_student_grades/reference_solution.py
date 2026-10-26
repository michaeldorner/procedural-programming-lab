def student_average(
    grades: dict[str,
    float],
) -> float:
    return sum(grades.values()) / len(grades)
