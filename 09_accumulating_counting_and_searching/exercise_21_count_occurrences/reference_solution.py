def count_occurrences(
    values: list[int],
    target: int,
) -> int:
    count = 0
    for value in values:
        if value == target:
            count += 1
    return count
