# Student template
def has_duplicates(
    values: list[int],
) -> bool:
    pass


# Basic solution
def has_duplicates(
    values: list[int],
) -> bool:
    return len(values) != len(set(values))


# Excellent solution for bonus tests
def has_duplicates(
    values: list[int],
) -> bool:
    return len(values) != len(set(values))
