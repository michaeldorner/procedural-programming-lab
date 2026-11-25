"""Lab 26: Linear Regression."""


def fit_linear_regression(
    xs: list[float],
    ys: list[float],
) -> tuple[float, float, float]:
    """Return (slope, intercept, r_squared) for ordinary least-squares fit.

    Raises:
        ValueError: If lengths differ, fewer than 2 points, or xs has zero variance.
    """
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("xs and ys must have equal length >= 2")
    mean_x: float = sum(xs) / len(xs)
    mean_y: float = sum(ys) / len(ys)
    ss_xx: float = sum((x - mean_x) ** 2 for x in xs)
    if ss_xx == 0.0:
        raise ValueError("xs must not have zero variance")
    ss_xy: float = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys, strict=True))
    slope: float = ss_xy / ss_xx
    intercept: float = mean_y - slope * mean_x
    ss_tot: float = sum((y - mean_y) ** 2 for y in ys)
    if ss_tot == 0.0:
        return (slope, intercept, 1.0)
    ss_res: float = sum(
        (y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys, strict=True)
    )
    return (slope, intercept, 1.0 - (ss_res / ss_tot))


if __name__ == "__main__":
    print(fit_linear_regression([1.0, 2.0, 3.0], [3.0, 5.0, 7.0]))
