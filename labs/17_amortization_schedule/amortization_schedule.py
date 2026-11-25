"""Lab 17: Amortization Schedule."""


def monthly_payment(principal: float, annual_rate: float, months: int) -> float:
    """Return fixed monthly payment for a loan.

    Raises:
        ValueError: If principal <= 0, annual_rate < 0, or months <= 0.
    """
    if principal <= 0.0 or annual_rate < 0.0 or months <= 0:
        raise ValueError("principal and months must be positive; annual_rate must be non-negative")
    if annual_rate == 0.0:
        return principal / months
    r: float = annual_rate / 12.0
    factor: float = (1.0 + r) ** months
    return principal * (r * factor) / (factor - 1.0)


def amortization_schedule(
    principal: float,
    annual_rate: float,
    months: int,
) -> list[tuple[int, float, float, float]]:
    """Return [(month, principal_paid, interest_paid, remaining_balance), ...]."""
    payment: float = monthly_payment(principal, annual_rate, months)
    r: float = annual_rate / 12.0
    balance: float = principal
    rows: list[tuple[int, float, float, float]] = []
    for month in range(1, months + 1):
        interest_paid: float = balance * r
        principal_paid: float = payment - interest_paid
        balance = max(0.0, balance - principal_paid)
        rows.append((month, round(principal_paid, 2), round(interest_paid, 2), round(balance, 2)))
    return rows


if __name__ == "__main__":
    print(amortization_schedule(1200.0, 0.06, 3))
