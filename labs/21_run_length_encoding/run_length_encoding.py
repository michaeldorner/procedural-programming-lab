"""Lab 21: Run-Length Encoding."""


def rle_encode(text: str) -> str | None:
    """Encode non-digit text using <count><char> runs, or return None if digits appear."""
    raise NotImplementedError


def rle_decode(encoded: str) -> str | None:
    """Decode <count><char> RLE text, or return None if malformed."""
    raise NotImplementedError


if __name__ == "__main__":
    enc = rle_encode("AAABBC")
    print("encoded:", enc, "decoded:", rle_decode(enc or ""))
