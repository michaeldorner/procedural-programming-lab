# Student template
def character_frequencies(
    text: str,
) -> dict[str, int]:
    pass


# Basic solution
def character_frequencies(
    text: str,
) -> dict[str, int]:
    frequencies = {}
    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1
    return frequencies


# Excellent solution for bonus tests
def character_frequencies(
    text: str,
) -> dict[str, int]:
    frequencies = {}
    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1
    return frequencies
