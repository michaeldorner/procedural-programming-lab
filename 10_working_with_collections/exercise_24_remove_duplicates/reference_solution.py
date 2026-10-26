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
