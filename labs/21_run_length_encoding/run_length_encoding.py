"""Lab 21: Run-Length Encoding."""


def rle_encode(text: str) -> str | None:
    """Encode non-digit text using <count><char> runs, or return None if digits appear."""
    if any(ch.isdigit() for ch in text):
        return None
    if not text:
        return ""
    parts: list[str] = []
    current: str = text[0]
    count: int = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            parts.append(f"{count}{current}")
            current = ch
            count = 1
    parts.append(f"{count}{current}")
    return "".join(parts)


def rle_decode(encoded: str) -> str | None:
    """Decode <count><char> RLE text, or return None if malformed."""
    if not encoded:
        return ""
    parts: list[str] = []
    count_digits: list[str] = []
    for ch in encoded:
        if ch.isdigit():
            count_digits.append(ch)
        else:
            if not count_digits:
                return None
            count: int = int("".join(count_digits))
            if count <= 0:
                return None
            parts.append(ch * count)
            count_digits.clear()
    if count_digits:
        return None
    return "".join(parts)


if __name__ == "__main__":
    enc = rle_encode("AAABBC")
    print("encoded:", enc, "decoded:", rle_decode(enc or ""))
