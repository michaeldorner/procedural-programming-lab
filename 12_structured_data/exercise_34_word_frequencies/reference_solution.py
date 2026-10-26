def word_frequencies(
    words: list[str],
) -> dict[str, int]:
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies
