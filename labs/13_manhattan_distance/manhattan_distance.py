"""Lab 13: Manhattan Distance."""


def calculate_manhattan_distance(
    coordinate_1: tuple[int, ...],
    coordinate_2: tuple[int, ...],
) -> int:
    """Return the n-dimensional Manhattan distance, raising ValueError if dimensions differ."""
    raise NotImplementedError


if __name__ == "__main__":
    print("2D:", calculate_manhattan_distance((1, 2), (4, 6)))
    print("3D:", calculate_manhattan_distance((-1, 0, 2), (2, -3, 2)))
