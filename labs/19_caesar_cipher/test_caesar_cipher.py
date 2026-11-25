"""Unit tests for caesar_cipher."""

import unittest

from .caesar_cipher import decrypt_caesar, encrypt_caesar


class TestCaesarCipher(unittest.TestCase):
    """Tests for Caesar cipher encryption and decryption."""

    def test_encrypt_and_decrypt(self) -> None:
        plain = "Hello, World! 123"
        encrypted = encrypt_caesar(plain, 3)
        self.assertEqual(encrypted, "Khoor, Zruog! 123")
        self.assertEqual(decrypt_caesar(encrypted, 3), plain)

    def test_wrap_around_and_negative_shift(self) -> None:
        self.assertEqual(encrypt_caesar("XYZxyz", 3), "ABCabc")
        self.assertEqual(encrypt_caesar("ABC", -3), "XYZ")
