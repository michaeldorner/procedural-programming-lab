import unittest

from solution import (
    most_frequent_word,
)


class MostFrequentWordTests(unittest.TestCase):

    def test_word_with_highest_frequency(
        self,
    ) -> None:
        words: list[str] = ["a", "b", "a", "c"]
        expected_word: str = "a"

        actual_word: str = most_frequent_word(
            words,
        )

        self.assertEqual(
            actual_word,
            expected_word,
        )

    def test_single_element_list(
        self,
    ) -> None:
        words: list[str] = ["x"]
        expected_word: str = "x"

        actual_word: str = most_frequent_word(
            words,
        )

        self.assertEqual(
            actual_word,
            expected_word,
        )


if __name__ == "__main__":
    unittest.main()
