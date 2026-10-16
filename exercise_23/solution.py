# Student template
def filter_even(
    values: list[int],
) -> list[int]:
    pass


# Basic solution
def filter_even(
    values: list[int],
) -> list[int]:
    result = []
    for value in values:
        if value % 2 == 0:
            result.append(value)
    return result


# Excellent solution for bonus tests
def filter_even(
    values: list[int],
) -> list[int]:
    result = []
    for value in values:
        if value % 2 == 0:
            result.append(value)
    return result
