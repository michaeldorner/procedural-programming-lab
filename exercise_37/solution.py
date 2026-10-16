# Student template
def lookup_phone(
    phone_book: dict[str,
    str],
    name: str,
) -> str:
    pass


# Basic solution
def lookup_phone(
    phone_book: dict[str,
    str],
    name: str,
) -> str:
    return phone_book.get(name, "")


# Excellent solution for bonus tests
def lookup_phone(
    phone_book: dict[str,
    str],
    name: str,
) -> str:
    return phone_book.get(name, "")
