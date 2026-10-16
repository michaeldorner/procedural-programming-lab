import unittest

from solution import (
    caesar_encrypt,
)


class Exercise49BonusTests(unittest.TestCase):

    def test_caesar_encrypt_1(
        self,
    ) -> None:
        value_0 = 'xyz'
        value_1 = 2
        expected_result = 'zab'

        actual_result = caesar_encrypt(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
