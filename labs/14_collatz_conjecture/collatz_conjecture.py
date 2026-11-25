"""Lab 14: Collatz Conjecture."""


def generate_collatz_sequence(start: int) -> list[int]:
    """Return the Collatz sequence from start down to 1.

Raises:
    ValueError: If start <= 0.
    """
    raise NotImplementedError


def count_collatz_steps(start: int) -> int:
    """Return number of Collatz steps from start to 1."""
    raise NotImplementedError


def find_collatz_peak(start: int) -> int:
    """Return maximum value in Collatz sequence starting at start."""
    raise NotImplementedError


if __name__ == "__main__":
    print("6:", generate_collatz_sequence(6), "steps:", count_collatz_steps(6), "peak:", find_collatz_peak(6))
