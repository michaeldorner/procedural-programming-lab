# Student template
def gcd(
    a: int,
    b: int,
) -> int:
    pass


# Basic solution
def gcd(
    a: int,
    b: int,
) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)


# Excellent solution for bonus tests
def gcd(
    a: int,
    b: int,
) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)
