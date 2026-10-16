# Student template
def common_elements(
    left: list[int],
    right: list[int],
) -> set[int]:
    pass


# Basic solution
def common_elements(
    left: list[int],
    right: list[int],
) -> set[int]:
    return set(left) & set(right)


# Excellent solution for bonus tests
def common_elements(
    left: list[int],
    right: list[int],
) -> set[int]:
    return set(left) & set(right)
