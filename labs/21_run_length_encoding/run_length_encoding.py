"""Lab 21: Run-Length Encoding."""


def encode_rle(text: str) -> str | None:
    """Encode non-digit text using <count><char> runs, or return None if digits appear."""
    raise NotImplementedError


def decode_rle(encoded: str) -> str | None:
    """Decode <count><char> RLE text, or return None if malformed."""
    raise NotImplementedError


if __name__ == "__main__":
    enc = encode_rle("AAABBC")
    print("encoded:", enc, "decoded:", decode_rle(enc or ""))
