def _normalize_isbn10(
    isbn: str,
) -> str:
    normalized = ""

    for character in isbn:
        if character in "- ":
            continue

        normalized += character.upper()

    return normalized


def is_valid_isbn10(
    isbn: str,
) -> bool:
    normalized = _normalize_isbn10(
        isbn,
    )

    if len(normalized) != 10:
        return False

    total = 0

    for index in range(10):
        character = normalized[index]

        if character == "X" and index == 9:
            digit = 10
        elif character.isdigit():
            digit = int(
                character,
            )
        else:
            return False

        weight = 10 - index
        total += digit * weight

    return total % 11 == 0
