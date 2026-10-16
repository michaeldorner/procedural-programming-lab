# Student template
def simple_csv_average(
    filename: str,
    column_index: int,
) -> float:
    pass


# Basic solution
def simple_csv_average(
    filename: str,
    column_index: int,
) -> float:
    values = []
    with open(filename, encoding="utf-8") as file:
        next(file)
        for line in file:
            columns = line.strip().split(",")
            values.append(float(columns[column_index]))
    return sum(values) / len(values)


# Excellent solution for bonus tests
def simple_csv_average(
    filename: str,
    column_index: int,
) -> float:
    values = []
    with open(filename, encoding="utf-8") as file:
        next(file)
        for line in file:
            columns = line.strip().split(",")
            values.append(float(columns[column_index]))
    return sum(values) / len(values)
