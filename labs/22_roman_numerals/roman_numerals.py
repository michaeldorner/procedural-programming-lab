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


def convert_int_to_roman(number: int) -> str | None:
    """Convert integer in [1, 3999] to canonical Roman numeral, or None if out of range."""
    raise NotImplementedError


def convert_roman_to_int(numeral: str) -> int | None:
    """Convert canonical Roman numeral to int, or None if invalid/non-canonical."""
    raise NotImplementedError


if __name__ == "__main__":
    print("1994 ->", convert_int_to_roman(1994), "back ->", convert_roman_to_int("MCMXCIV"))
