"""Lab 18: Slug Normalizer."""


def to_slug(raw_title: str) -> str:
    """Convert raw_title into a lowercase ASCII hyphen-separated slug."""
    chars: list[str] = []
    prev_hyphen: bool = True
    for ch in raw_title.lower():
        if ch.isascii() and ch.isalnum():
            chars.append(ch)
            prev_hyphen = False
        elif not prev_hyphen:
            chars.append("-")
            prev_hyphen = True
    return "".join(chars).strip("-")


if __name__ == "__main__":
    print(to_slug("  Hello, World!  2026 "))
