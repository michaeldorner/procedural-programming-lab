import unittest

from solution import (
    caesar_encrypt,
)


class CaesarCipherTests(unittest.TestCase):

    def test_shift_without_wrap(
        self,
    ) -> None:
        plaintext: str = "abc"
        shift_amount: int = 1
        expected_ciphertext: str = "bcd"

        actual_ciphertext: str = caesar_encrypt(
            plaintext,
            shift_amount,
        )

        self.assertEqual(
            actual_ciphertext,
            expected_ciphertext,
        )

    def test_shift_with_alphabet_wrap(
        self,
    ) -> None:
        plaintext: str = "xyz"
        shift_amount: int = 2
        expected_ciphertext: str = "zab"

        actual_ciphertext: str = caesar_encrypt(
            plaintext,
            shift_amount,
        )

        self.assertEqual(
            actual_ciphertext,
            expected_ciphertext,
        )


if __name__ == "__main__":
    unittest.main()
