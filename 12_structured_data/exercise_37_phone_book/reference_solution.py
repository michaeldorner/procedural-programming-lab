def lookup_phone(
    phone_book: dict[str,
    str],
    name: str,
) -> str:
    return phone_book.get(name, "")
