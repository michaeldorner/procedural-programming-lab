# Student template
def count_lines(
    filename: str,
) -> int:
    pass


# Basic solution
def count_lines(
    filename: str,
) -> int:
    with open(filename, encoding="utf-8") as file:
        return len(file.readlines())


# Excellent solution for bonus tests
def count_lines(
    filename: str,
) -> int:
    with open(filename, encoding="utf-8") as file:
        return len(file.readlines())
