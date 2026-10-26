def most_frequent_word(
    words: list[str],
) -> str:
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return max(frequencies, key=frequencies.get)
