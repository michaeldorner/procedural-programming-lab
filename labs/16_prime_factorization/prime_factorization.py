"""Lab 16: Prime Factorization."""


def factorize_primes(number: int) -> list[int]:
    """Return sorted prime factors of number >= 2.

Raises:
    ValueError: If number < 2.
    """
    raise NotImplementedError


def is_prime(number: int) -> bool:
    """Return True if number is prime."""
    raise NotImplementedError


if __name__ == "__main__":
    print("84:", factorize_primes(84), "29 prime:", is_prime(29))
