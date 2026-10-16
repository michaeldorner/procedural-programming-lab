# Student template
def linear_search(
    values: list[int],
    target: int,
) -> int:
    pass


# Basic solution
def linear_search(
    values: list[int],
    target: int,
) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


# Excellent solution for bonus tests
def linear_search(
    values: list[int],
    target: int,
) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1
