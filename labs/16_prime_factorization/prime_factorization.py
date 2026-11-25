"""Lab 16: Prime Factorization."""


def prime_factors(number: int) -> list[int]:
    """Return sorted prime factors of number >= 2.

    Raises:
        ValueError: If number < 2.
    """
    if number < 2:
        raise ValueError(f"number must be >= 2, got {number}")
    factors: list[int] = []
    remaining: int = number
    divisor: int = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.append(remaining)
    return factors


def is_prime(number: int) -> bool:
    """Return True if number is prime."""
    if number < 2:
        return False
    return len(prime_factors(number)) == 1


if __name__ == "__main__":
    print("84:", prime_factors(84), "29 prime:", is_prime(29))
