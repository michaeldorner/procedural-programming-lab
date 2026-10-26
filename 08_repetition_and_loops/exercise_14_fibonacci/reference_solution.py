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
