"""Lab 14: Collatz Conjecture."""


def collatz_sequence(start: int) -> list[int]:
    """Return the Collatz sequence from start down to 1.

    Raises:
        ValueError: If start <= 0.
    """
    if start <= 0:
        raise ValueError(f"start must be positive, got {start}")
    seq: list[int] = [start]
    current: int = start
    while current != 1:
        current = current // 2 if current % 2 == 0 else 3 * current + 1
        seq.append(current)
    return seq


def collatz_stopping_time(start: int) -> int:
    """Return number of Collatz steps from start to 1."""
    return len(collatz_sequence(start)) - 1


def collatz_peak(start: int) -> int:
    """Return maximum value in Collatz sequence starting at start."""
    return max(collatz_sequence(start))


if __name__ == "__main__":
    print("6:", collatz_sequence(6), "steps:", collatz_stopping_time(6), "peak:", collatz_peak(6))
