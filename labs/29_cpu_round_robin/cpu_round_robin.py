"""Lab 29: CPU Round-Robin."""

from collections import deque


def round_robin_completion_times(burst_times: list[int], quantum: int) -> list[int]:
    """Return completion times per process under Round-Robin scheduling.

    Raises:
        ValueError: If quantum <= 0 or any burst time <= 0.
    """
    if quantum <= 0 or any(b <= 0 for b in burst_times):
        raise ValueError("quantum and all burst_times must be positive")
    if not burst_times:
        return []
    queue: deque[tuple[int, int]] = deque(
        (idx, burst) for idx, burst in enumerate(burst_times)
    )
    completion: list[int] = [0] * len(burst_times)
    clock: int = 0
    while queue:
        idx, remaining = queue.popleft()
        step: int = min(quantum, remaining)
        clock += step
        remaining -= step
        if remaining == 0:
            completion[idx] = clock
        else:
            queue.append((idx, remaining))
    return completion


if __name__ == "__main__":
    print(round_robin_completion_times([5, 3, 1], 2))
