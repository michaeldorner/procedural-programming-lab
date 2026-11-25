"""Lab 19: Caesar Cipher."""


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt ASCII letters in text by shift positions, preserving case and non-letters."""
    result: list[str] = []
    for ch in text:
        if "A" <= ch <= "Z":
            offset: int = (ord(ch) - ord("A") + shift) % 26
            result.append(chr(ord("A") + offset))
        elif "a" <= ch <= "z":
            offset = (ord(ch) - ord("a") + shift) % 26
            result.append(chr(ord("a") + offset))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text encrypted with caesar_encrypt(text, shift)."""
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    secret = caesar_encrypt("Hello, World!", 3)
    print("encrypted:", secret, "decrypted:", caesar_decrypt(secret, 3))
