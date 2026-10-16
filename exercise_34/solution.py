# Student template
def word_frequencies(
    words: list[str],
) -> dict[str, int]:
    pass


# Basic solution
def word_frequencies(
    words: list[str],
) -> dict[str, int]:
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


# Excellent solution for bonus tests
def word_frequencies(
    words: list[str],
) -> dict[str, int]:
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies
