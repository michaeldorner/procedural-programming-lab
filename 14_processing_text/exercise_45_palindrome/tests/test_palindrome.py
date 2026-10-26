import unittest

from solution import (
    is_palindrome,
)


class PalindromeTests(unittest.TestCase):

    def test_palindrome_word(
        self,
    ) -> None:
        candidate_word: str = "level"

        palindrome_status: bool = is_palindrome(
            candidate_word,
        )

        self.assertTrue(
            palindrome_status,
        )

    def test_non_palindrome_word(
        self,
    ) -> None:
        candidate_word: str = "python"

        palindrome_status: bool = is_palindrome(
            candidate_word,
        )

        self.assertFalse(
            palindrome_status,
        )

    def test_empty_string_is_palindrome(
        self,
    ) -> None:
        candidate_word: str = ""

        palindrome_status: bool = is_palindrome(
            candidate_word,
        )

        self.assertTrue(
            palindrome_status,
        )


if __name__ == "__main__":
    unittest.main()
