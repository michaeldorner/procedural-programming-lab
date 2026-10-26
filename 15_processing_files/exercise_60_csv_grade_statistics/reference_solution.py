def csv_grade_statistics(
    filename: str,
) -> tuple[float, float, float]:
    grades = []
    with open(filename, encoding="utf-8") as file:
        next(file)
        for line in file:
            _, grade = line.strip().split(",")
            grades.append(float(grade))
    return sum(grades) / len(grades), min(grades), max(grades)
