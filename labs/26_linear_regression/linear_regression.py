"""Lab 26: Linear Regression."""


def fit_linear_regression(
    xs: list[float],
    ys: list[float],
) -> tuple[float, float, float]:
    """Return (slope, intercept, r_squared) for ordinary least-squares fit.

Raises:
    ValueError: If lengths differ, fewer than 2 points, or xs has zero variance.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(fit_linear_regression([1.0, 2.0, 3.0], [3.0, 5.0, 7.0]))
