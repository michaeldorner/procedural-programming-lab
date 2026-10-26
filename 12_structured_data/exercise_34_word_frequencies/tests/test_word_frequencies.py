import unittest

from solution import (
    word_frequencies,
)


class WordFrequenciesTests(unittest.TestCase):

    def test_list_with_repeated_words(
        self,
    ) -> None:
        words: list[str] = ["apple", "banana", "apple"]
        expected_counts: dict[str, int] = {"apple": 2, "banana": 1}

        actual_counts: dict[str, int] = word_frequencies(
            words,
        )

        self.assertEqual(
            actual_counts,
            expected_counts,
        )

    def test_empty_word_list(
        self,
    ) -> None:
        words: list[str] = []
        expected_counts: dict[str, int] = {}

        actual_counts: dict[str, int] = word_frequencies(
            words,
        )

        self.assertEqual(
            actual_counts,
            expected_counts,
        )


if __name__ == "__main__":
    unittest.main()
