"""Lab 09: ATM Dispenser."""


def dispense_banknotes(
    amount_eur: int,
    account_balance: int,
) -> tuple[int, int, int, int] | None:
    """Return (100s, 50s, 20s, 10s) banknote counts, or None on insufficient funds.

Raises:
    ValueError: If amount_eur <= 0, account_balance < 0, or amount_eur % 10 != 0.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print("180 EUR:", dispense_banknotes(180, 500))
