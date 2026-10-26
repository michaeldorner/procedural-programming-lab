def count_vowels(
    text: str,
) -> int:
    count = 0
    for character in text.lower():
        if character in "aeiou":
            count += 1
    return count
