# Student template
def count_by_grade(
    students: list[dict[str,
    str]],
) -> dict[str, int]:
    pass


# Basic solution
def count_by_grade(
    students: list[dict[str,
    str]],
) -> dict[str, int]:
    counts = {}
    for student in students:
        grade = student["grade"]
        counts[grade] = counts.get(grade, 0) + 1
    return counts


# Excellent solution for bonus tests
def count_by_grade(
    students: list[dict[str,
    str]],
) -> dict[str, int]:
    counts = {}
    for student in students:
        grade = student["grade"]
        counts[grade] = counts.get(grade, 0) + 1
    return counts
