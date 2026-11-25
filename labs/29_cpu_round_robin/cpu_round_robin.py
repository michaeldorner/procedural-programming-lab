"""Lab 29: CPU Round-Robin."""


def round_robin_completion_times(burst_times: list[int], quantum: int) -> list[int]:
    """Return completion times per process under Round-Robin scheduling.

Raises:
    ValueError: If quantum <= 0 or any burst time <= 0.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(round_robin_completion_times([5, 3, 1], 2))
