"""Lab 15: Compound Interest."""


def simulate_yearly_balances(principal: float, annual_rate: float, years: int) -> list[float]:
    """Return [year_0, ..., year_N] balances rounded to 2 decimals.

Raises:
    ValueError: If principal < 0, annual_rate < 0, or years < 0.
    """
    raise NotImplementedError


def count_years_to_target(principal: float, annual_rate: float, target: float) -> int | None:
    """Return whole years until principal reaches >= target, or None if unreachable.

Raises:
    ValueError: If principal <= 0, annual_rate < 0, or target < 0.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print("2 yrs:", simulate_yearly_balances(1000.0, 0.05, 2))
    print("years to 1200:", count_years_to_target(1000.0, 0.10, 1200.0))
