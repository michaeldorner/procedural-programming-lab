import unittest

from solution import (
    is_palindrome,
)


class Exercise45RequiredTests(unittest.TestCase):

    def test_is_palindrome_1(
        self,
    ) -> None:
        value_0 = 'level'
        expected_result = True

        actual_result = is_palindrome(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_is_palindrome_2(
        self,
    ) -> None:
        value_0 = 'python'
        expected_result = False

        actual_result = is_palindrome(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
