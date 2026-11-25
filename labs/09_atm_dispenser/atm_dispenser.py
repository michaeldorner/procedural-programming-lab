"""Lab 09: ATM Dispenser."""


def dispense_banknotes(
    amount_eur: int,
    account_balance: int,
) -> tuple[int, int, int, int] | None:
    """Return (100s, 50s, 20s, 10s) banknote counts, or None on insufficient funds.

    Raises:
        ValueError: If amount_eur <= 0, account_balance < 0, or amount_eur % 10 != 0.
    """
    if amount_eur <= 0:
        raise ValueError(f"amount_eur must be positive, got {amount_eur}")
    if account_balance < 0:
        raise ValueError(f"account_balance must be non-negative, got {account_balance}")
    if amount_eur % 10 != 0:
        raise ValueError(f"amount_eur must be a multiple of 10, got {amount_eur}")
    if amount_eur > account_balance:
        return None

    remaining: int = amount_eur
    n100: int = remaining // 100
    remaining %= 100
    n50: int = remaining // 50
    remaining %= 50
    n20: int = remaining // 20
    remaining %= 20
    n10: int = remaining // 10
    return (n100, n50, n20, n10)


if __name__ == "__main__":
    print("180 EUR:", dispense_banknotes(180, 500))
