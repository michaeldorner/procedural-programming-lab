"""Lab 02: Egg Carton Packer."""


def count_full_cartons(eggs: int, capacity: int) -> int:
    """Return the number of completely filled cartons."""
    raise NotImplementedError


def count_loose_eggs(eggs: int, capacity: int) -> int:
    """Return the remaining eggs after filling complete cartons."""
    raise NotImplementedError


def calculate_minimum_cartons(eggs: int, capacity: int) -> int:
    """Return the minimum cartons needed to hold all eggs (ceiling division)."""
    raise NotImplementedError


if __name__ == "__main__":
    print(
        "26 eggs (cap 12):",
        count_full_cartons(26, 12),
        count_loose_eggs(26, 12),
        calculate_minimum_cartons(26, 12),
    )
