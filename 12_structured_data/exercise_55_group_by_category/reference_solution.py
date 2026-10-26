def group_by_category(
    items: list[dict[str,
    str]],
) -> dict[str, list[str]]:
    groups = {}
    for item in items:
        category = item["category"]
        groups.setdefault(category, []).append(item["name"])
    return groups
