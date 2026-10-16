# Student template
def update_inventory(
    inventory: dict[str,
    int],
    item: str,
    amount: int,
) -> dict[str, int]:
    pass


# Basic solution
def update_inventory(
    inventory: dict[str,
    int],
    item: str,
    amount: int,
) -> dict[str, int]:
    inventory[item] = inventory.get(item, 0) + amount
    return inventory


# Excellent solution for bonus tests
def update_inventory(
    inventory: dict[str,
    int],
    item: str,
    amount: int,
) -> dict[str, int]:
    inventory[item] = inventory.get(item, 0) + amount
    return inventory
