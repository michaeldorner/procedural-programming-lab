def update_inventory(
    inventory: dict[str,
    int],
    item: str,
    amount: int,
) -> dict[str, int]:
    inventory[item] = inventory.get(item, 0) + amount
    return inventory
