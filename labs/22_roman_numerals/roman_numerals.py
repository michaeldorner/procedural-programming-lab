"""Lab 22: Roman Numerals."""

_ROMAN_TABLE: tuple[tuple[int, str], ...] = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)

_VALUES_BY_SYMBOL: dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def int_to_roman(number: int) -> str | None:
    """Convert integer in [1, 3999] to canonical Roman numeral, or None if out of range."""
    if number < 1 or number > 3999:
        return None
    remaining: int = number
    parts: list[str] = []
    for value, symbol in _ROMAN_TABLE:
        while remaining >= value:
            parts.append(symbol)
            remaining -= value
    return "".join(parts)


def roman_to_int(numeral: str) -> int | None:
    """Convert canonical Roman numeral to int, or None if invalid/non-canonical."""
    cleaned: str = numeral.strip().upper()
    if not cleaned:
        return None
    total: int = 0
    idx: int = 0
    while idx < len(cleaned):
        curr = _VALUES_BY_SYMBOL.get(cleaned[idx])
        if curr is None:
            return None
        if idx + 1 < len(cleaned):
            nxt = _VALUES_BY_SYMBOL.get(cleaned[idx + 1])
            if nxt is None:
                return None
            if nxt > curr:
                total += nxt - curr
                idx += 2
                continue
        total += curr
        idx += 1
    if int_to_roman(total) != cleaned:
        return None
    return total


if __name__ == "__main__":
    print("1994 ->", int_to_roman(1994), "back ->", roman_to_int("MCMXCIV"))
