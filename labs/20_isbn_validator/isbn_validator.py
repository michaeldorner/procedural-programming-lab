"""Lab 20: ISBN Validator."""


def is_valid_isbn10(raw_isbn: str) -> bool:
    """Return True if raw_isbn is a valid ISBN-10."""
    raise NotImplementedError


def is_valid_isbn13(raw_isbn: str) -> bool:
    """Return True if raw_isbn is a valid ISBN-13."""
    raise NotImplementedError


if __name__ == "__main__":
    print("ISBN-10:", is_valid_isbn10("0-306-40615-2"))
    print("ISBN-13:", is_valid_isbn13("978-0-306-40615-7"))
