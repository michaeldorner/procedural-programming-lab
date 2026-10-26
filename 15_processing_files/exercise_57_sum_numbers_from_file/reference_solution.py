def sum_numbers_from_file(
    filename: str,
) -> float:
    total = 0.0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            total += float(line.strip())
    return total
