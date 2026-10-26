def library_search(
    books: list[dict[str,
    str]],
    title: str,
) -> dict[str, str] | None:
    for book in books:
        if book["title"] == title:
            return book
    return None
