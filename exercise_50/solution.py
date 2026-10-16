# Student template
def count_first_quadrant(
    points: list[tuple[float,
    float]],
) -> int:
    pass


# Basic solution
def count_first_quadrant(
    points: list[tuple[float,
    float]],
) -> int:
    count = 0
    for x, y in points:
        if x > 0 and y > 0:
            count += 1
    return count


# Excellent solution for bonus tests
def count_first_quadrant(
    points: list[tuple[float,
    float]],
) -> int:
    count = 0
    for x, y in points:
        if x > 0 and y > 0:
            count += 1
    return count
