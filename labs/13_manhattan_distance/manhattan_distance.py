"""Lab 13: Manhattan Distance."""


def calculate_manhattan_distance(
    coordinate_1: tuple[int, ...],
    coordinate_2: tuple[int, ...],
) -> int:
    """Return the n-dimensional Manhattan distance, raising ValueError if dimensions differ."""
    if len(coordinate_1) != len(coordinate_2):
        raise ValueError(
            f"Coordinates must have the same dimension (got {len(coordinate_1)} and {len(coordinate_2)})"
        )
    total: int = 0
    for i in range(len(coordinate_1)):
        total += abs(coordinate_1[i] - coordinate_2[i])
    return total

    # Optional alternative using zip():
    # return sum(abs(a - b) for a, b in zip(coordinate_1, coordinate_2, strict=True))


if __name__ == "__main__":
    print("2D:", calculate_manhattan_distance((1, 2), (4, 6)))
    print("3D:", calculate_manhattan_distance((-1, 0, 2), (2, -3, 2)))
