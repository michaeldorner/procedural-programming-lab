"""Lab 23: Moving Average."""


def simple_moving_average(values: list[float], window: int) -> list[float]:
    """Return sliding window averages of length window.

    Raises:
        ValueError: If window <= 0.
    """
    if window <= 0:
        raise ValueError(f"window must be positive, got {window}")
    if len(values) < window:
        return []
    return [
        sum(values[idx : idx + window]) / window
        for idx in range(len(values) - window + 1)
    ]


if __name__ == "__main__":
    print(simple_moving_average([1.0, 2.0, 3.0, 4.0], 2))
