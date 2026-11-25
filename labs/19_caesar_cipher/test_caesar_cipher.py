"""Unit tests for caesar_cipher."""

import unittest

from caesar_cipher import caesar_decrypt, caesar_encrypt


class TestCaesarCipher(unittest.TestCase):
    """Tests for Caesar cipher encryption and decryption."""

    def test_encrypt_and_decrypt(self) -> None:
        plain = "Hello, World! 123"
        encrypted = caesar_encrypt(plain, 3)
        self.assertEqual(encrypted, "Khoor, Zruog! 123")
        self.assertEqual(caesar_decrypt(encrypted, 3), plain)

    def test_wrap_around_and_negative_shift(self) -> None:
        self.assertEqual(caesar_encrypt("XYZxyz", 3), "ABCabc")
        self.assertEqual(caesar_encrypt("ABC", -3), "XYZ")
