def longest_word(
    text: str,
) -> str:
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)
