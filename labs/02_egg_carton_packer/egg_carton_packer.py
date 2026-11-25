"""Lab 02: Egg Carton Packer."""


def full_cartons(eggs: int, capacity: int) -> int:
    """Return the number of completely filled cartons."""
    raise NotImplementedError


def loose_eggs(eggs: int, capacity: int) -> int:
    """Return the remaining eggs after filling complete cartons."""
    raise NotImplementedError


def minimum_cartons_needed(eggs: int, capacity: int) -> int:
    """Return the minimum cartons needed to hold all eggs (ceiling division)."""
    raise NotImplementedError


if __name__ == "__main__":
    print(
        "26 eggs (cap 12):",
        full_cartons(26, 12),
        loose_eggs(26, 12),
        minimum_cartons_needed(26, 12),
    )
