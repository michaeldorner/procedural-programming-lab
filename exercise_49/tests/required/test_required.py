import unittest

from solution import (
    caesar_encrypt,
)


class Exercise49RequiredTests(unittest.TestCase):

    def test_caesar_encrypt_1(
        self,
    ) -> None:
        value_0 = 'abc'
        value_1 = 1
        expected_result = 'bcd'

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
