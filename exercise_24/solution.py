# Student template
def remove_duplicates(
    values: list[int],
) -> list[int]:
    pass


# Basic solution
def remove_duplicates(
    values: list[int],
) -> list[int]:
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result


# Excellent solution for bonus tests
def remove_duplicates(
    values: list[int],
) -> list[int]:
    result = []
    seen = set()
    for value in values:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return result
