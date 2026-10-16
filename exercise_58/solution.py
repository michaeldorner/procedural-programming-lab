# Student template
def word_frequencies_from_file(
    filename: str,
) -> dict[str, int]:
    pass


# Basic solution
def word_frequencies_from_file(
    filename: str,
) -> dict[str, int]:
    frequencies = {}
    with open(filename, encoding="utf-8") as file:
        for word in file.read().split():
            frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


# Excellent solution for bonus tests
def word_frequencies_from_file(
    filename: str,
) -> dict[str, int]:
    frequencies = {}
    with open(filename, encoding="utf-8") as file:
        for word in file.read().split():
            frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies
