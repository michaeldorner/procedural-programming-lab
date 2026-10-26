def min_max(
    values: list[int],
) -> tuple[int, int]:
    minimum = values[0]
    maximum = values[0]
    for value in values[1:]:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
    return minimum, maximum
