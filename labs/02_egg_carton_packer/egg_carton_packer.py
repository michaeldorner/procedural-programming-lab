"""Lab 02: Egg Carton Packer."""


def _validate_inputs(eggs: int, capacity: int) -> None:
    """Raise ValueError if eggs is negative or capacity is non-positive."""
    if eggs < 0:
        raise ValueError(f"eggs must be non-negative, got {eggs}")
    if capacity <= 0:
        raise ValueError(f"capacity must be positive, got {capacity}")


def full_cartons(eggs: int, capacity: int) -> int:
    """Return the number of completely filled cartons."""
    _validate_inputs(eggs, capacity)
    return eggs // capacity


def loose_eggs(eggs: int, capacity: int) -> int:
    """Return the remaining eggs after filling complete cartons."""
    _validate_inputs(eggs, capacity)
    return eggs % capacity


def minimum_cartons_needed(eggs: int, capacity: int) -> int:
    """Return the minimum cartons needed to hold all eggs (ceiling division)."""
    _validate_inputs(eggs, capacity)
    return (eggs + capacity - 1) // capacity


if __name__ == "__main__":
    print(
        "26 eggs (cap 12):",
        full_cartons(26, 12),
        loose_eggs(26, 12),
        minimum_cartons_needed(26, 12),
    )
