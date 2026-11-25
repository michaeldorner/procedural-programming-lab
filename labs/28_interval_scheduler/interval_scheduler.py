"""Lab 28: Interval Scheduler."""


def select_max_meetings(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Select maximum non-overlapping (start, end) intervals.

Raises:
    ValueError: If any interval has start >= end.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(select_max_meetings([(1, 4), (3, 5), (0, 6), (5, 7)]))
