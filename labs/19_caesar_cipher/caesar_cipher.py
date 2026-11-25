"""Lab 19: Caesar Cipher."""


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt ASCII letters in text by shift positions, preserving case and non-letters."""
    raise NotImplementedError


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text encrypted with caesar_encrypt(text, shift)."""
    raise NotImplementedError


if __name__ == "__main__":
    secret = caesar_encrypt("Hello, World!", 3)
    print("encrypted:", secret, "decrypted:", caesar_decrypt(secret, 3))
