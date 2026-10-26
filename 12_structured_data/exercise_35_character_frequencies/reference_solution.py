def character_frequencies(
    text: str,
) -> dict[str, int]:
    frequencies = {}
    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1
    return frequencies
