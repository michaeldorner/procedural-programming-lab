"""Lab 19: Caesar Cipher."""


def encrypt_caesar(text: str, shift: int) -> str:
    """Encrypt ASCII letters in text by shift positions, preserving case and non-letters."""
    raise NotImplementedError


def decrypt_caesar(text: str, shift: int) -> str:
    """Decrypt text encrypted with encrypt_caesar(text, shift)."""
    raise NotImplementedError


if __name__ == "__main__":
    secret = encrypt_caesar("Hello, World!", 3)
    print("encrypted:", secret, "decrypted:", decrypt_caesar(secret, 3))
