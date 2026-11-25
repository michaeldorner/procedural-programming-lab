"""Lab 20: ISBN Validator."""


def is_valid_isbn10(raw_isbn: str) -> bool:
    """Return True if raw_isbn is a valid ISBN-10."""
    cleaned: str = raw_isbn.strip().replace("-", "").upper()
    if len(cleaned) != 10:
        return False
    total: int = 0
    for idx, ch in enumerate(cleaned):
        if idx == 9 and ch == "X":
            digit = 10
        elif ch.isdigit():
            digit = int(ch)
        else:
            return False
        total += (10 - idx) * digit
    return total % 11 == 0


def is_valid_isbn13(raw_isbn: str) -> bool:
    """Return True if raw_isbn is a valid ISBN-13."""
    cleaned: str = raw_isbn.strip().replace("-", "")
    if len(cleaned) != 13 or not cleaned.isdigit():
        return False
    total: int = 0
    for idx, ch in enumerate(cleaned):
        weight: int = 1 if idx % 2 == 0 else 3
        total += weight * int(ch)
    return total % 10 == 0


if __name__ == "__main__":
    print("ISBN-10:", is_valid_isbn10("0-306-40615-2"))
    print("ISBN-13:", is_valid_isbn13("978-0-306-40615-7"))
