def count_lines(
    filename: str,
) -> int:
    with open(filename, encoding="utf-8") as file:
        return len(file.readlines())
