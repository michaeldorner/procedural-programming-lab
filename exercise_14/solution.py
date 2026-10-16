# Student template
def fibonacci(
    n: int,
) -> int:
    pass


# Basic solution
def fibonacci(
    n: int,
) -> int:
    if n == 0:
        return 0
    previous = 0
    current = 1
    for _ in range(1, n):
        previous, current = current, previous + current
    return current


# Excellent solution for bonus tests
def fibonacci(
    n: int,
) -> int:
    if n == 0:
        return 0
    previous = 0
    current = 1
    for _ in range(1, n):
        previous, current = current, previous + current
    return current
