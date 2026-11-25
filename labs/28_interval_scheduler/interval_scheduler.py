"""Lab 28: Interval Scheduler."""


def select_max_meetings(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Select maximum non-overlapping (start, end) intervals.

    Raises:
        ValueError: If any interval has start >= end.
    """
    if any(start >= end for start, end in intervals):
        raise ValueError("Every interval must satisfy start < end")
    ordered: list[tuple[int, int]] = sorted(intervals, key=lambda pair: (pair[1], pair[0]))
    selected: list[tuple[int, int]] = []
    last_end: int | None = None
    for start, end in ordered:
        if last_end is None or start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected


if __name__ == "__main__":
    print(select_max_meetings([(1, 4), (3, 5), (0, 6), (5, 7)]))
