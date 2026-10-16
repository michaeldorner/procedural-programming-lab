# Student template
def longest_word(
    text: str,
) -> str:
    pass


# Basic solution
def longest_word(
    text: str,
) -> str:
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


# Excellent solution for bonus tests
def longest_word(
    text: str,
) -> str:
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)
