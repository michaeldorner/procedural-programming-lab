"""Lab 18: Slug Normalizer."""


def to_slug(raw_title: str) -> str:
    """Convert raw_title into a lowercase ASCII hyphen-separated slug."""
    raise NotImplementedError


if __name__ == "__main__":
    print(to_slug("  Hello, World!  2026 "))
