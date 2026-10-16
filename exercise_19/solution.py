# Student template
def maximum(
    values: list[int],
) -> int:
    pass


# Basic solution
def maximum(
    values: list[int],
) -> int:
    result = values[0]
    for value in values[1:]:
        if value > result:
            result = value
    return result


# Excellent solution for bonus tests
def maximum(
    values: list[int],
) -> int:
    result = values[0]
    for value in values[1:]:
        if value > result:
            result = value
    return result
