def has_duplicates(
    values: list[int],
) -> bool:
    return len(values) != len(set(values))
