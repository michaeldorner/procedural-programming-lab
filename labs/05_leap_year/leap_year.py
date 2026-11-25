"""Lab 05: Leap Year."""


def is_leap_year(year: int) -> bool:
    """Return True if year is a valid Gregorian leap year, else False."""
    return year > 0 and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))


if __name__ == "__main__":
    print("2000:", is_leap_year(2000))
    print("1900:", is_leap_year(1900))
    print("2024:", is_leap_year(2024))
