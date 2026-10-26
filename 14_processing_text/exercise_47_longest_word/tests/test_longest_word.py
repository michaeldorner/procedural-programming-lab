import unittest

from solution import (
    longest_word,
)


class LongestWordTests(unittest.TestCase):

    def test_finds_longest_in_sentence(
        self,
    ) -> None:
        sentence: str = "one three two"
        expected_word: str = "three"

        actual_word: str = longest_word(
            sentence,
        )

        self.assertEqual(
            actual_word,
            expected_word,
        )

    def test_empty_string_returns_empty(
        self,
    ) -> None:
        sentence: str = ""
        expected_word: str = ""

        actual_word: str = longest_word(
            sentence,
        )

        self.assertEqual(
            actual_word,
            expected_word,
        )


if __name__ == "__main__":
    unittest.main()
