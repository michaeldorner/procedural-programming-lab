"""Lab 15: Compound Interest."""


def yearly_balances(principal: float, annual_rate: float, years: int) -> list[float]:
    """Return [year_0, ..., year_N] balances rounded to 2 decimals.

    Raises:
        ValueError: If principal < 0, annual_rate < 0, or years < 0.
    """
    if principal < 0.0 or annual_rate < 0.0 or years < 0:
        raise ValueError("principal, annual_rate, and years must be non-negative")
    balances: list[float] = [round(principal, 2)]
    current: float = principal
    for _ in range(years):
        current *= 1.0 + annual_rate
        balances.append(round(current, 2))
    return balances


def years_to_target(principal: float, annual_rate: float, target: float) -> int | None:
    """Return whole years until principal reaches >= target, or None if unreachable.

    Raises:
        ValueError: If principal <= 0, annual_rate < 0, or target < 0.
    """
    if principal <= 0.0 or annual_rate < 0.0 or target < 0.0:
        raise ValueError("principal must be positive and annual_rate/target non-negative")
    if principal >= target:
        return 0
    if annual_rate == 0.0:
        return None
    years: int = 0
    current: float = principal
    while current < target:
        current *= 1.0 + annual_rate
        years += 1
    return years


if __name__ == "__main__":
    print("2 yrs:", yearly_balances(1000.0, 0.05, 2))
    print("years to 1200:", years_to_target(1000.0, 0.10, 1200.0))
