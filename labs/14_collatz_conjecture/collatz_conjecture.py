"""Lab 14: Collatz Conjecture."""


def collatz_sequence(start: int) -> list[int]:
    """Return the Collatz sequence from start down to 1.

Raises:
    ValueError: If start <= 0.
    """
    raise NotImplementedError


def collatz_stopping_time(start: int) -> int:
    """Return number of Collatz steps from start to 1."""
    raise NotImplementedError


def collatz_peak(start: int) -> int:
    """Return maximum value in Collatz sequence starting at start."""
    raise NotImplementedError


if __name__ == "__main__":
    print("6:", collatz_sequence(6), "steps:", collatz_stopping_time(6), "peak:", collatz_peak(6))
