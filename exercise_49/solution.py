# Student template
def caesar_encrypt(
    text: str,
    shift: int,
) -> str:
    pass


# Basic solution
def caesar_encrypt(
    text: str,
    shift: int,
) -> str:
    result = ""
    for character in text:
        offset = (ord(character) - ord("a") + shift) % 26
        result += chr(ord("a") + offset)
    return result


# Excellent solution for bonus tests
def caesar_encrypt(
    text: str,
    shift: int,
) -> str:
    result = ""
    for character in text:
        offset = (ord(character) - ord("a") + shift) % 26
        result += chr(ord("a") + offset)
    return result
