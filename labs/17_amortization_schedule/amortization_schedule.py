"""Lab 17: Amortization Schedule."""


def monthly_payment(principal: float, annual_rate: float, months: int) -> float:
    """Return fixed monthly payment for a loan.

Raises:
    ValueError: If principal <= 0, annual_rate < 0, or months <= 0.
    """
    raise NotImplementedError


def amortization_schedule(
    principal: float,
    annual_rate: float,
    months: int,
) -> list[tuple[int, float, float, float]]:
    """Return [(month, principal_paid, interest_paid, remaining_balance), ...]."""
    raise NotImplementedError


if __name__ == "__main__":
    print(amortization_schedule(1200.0, 0.06, 3))
