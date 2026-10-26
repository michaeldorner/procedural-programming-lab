def contact_search(
    contacts: list[dict[str,
    str]],
    name: str,
) -> dict[str, str] | None:
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None
