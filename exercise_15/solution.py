# Student template
def is_prime(
    n: int,
) -> bool:
    pass


# Basic solution
def is_prime(
    n: int,
) -> bool:
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


# Excellent solution for bonus tests
def is_prime(
    n: int,
) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True
