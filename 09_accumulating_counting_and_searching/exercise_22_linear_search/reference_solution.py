def linear_search(
    values: list[int],
    target: int,
) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1
