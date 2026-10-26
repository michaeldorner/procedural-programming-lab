import unittest

from solution import (
    character_frequencies,
)


class CharacterFrequenciesTests(unittest.TestCase):

    def test_word_with_repeated_characters(
        self,
    ) -> None:
        text: str = "hello"
        expected_counts: dict[str, int] = {"h": 1, "e": 1, "l": 2, "o": 1}

        actual_counts: dict[str, int] = character_frequencies(
            text,
        )

        self.assertEqual(
            actual_counts,
            expected_counts,
        )

    def test_empty_string(
        self,
    ) -> None:
        text: str = ""
        expected_counts: dict[str, int] = {}

        actual_counts: dict[str, int] = character_frequencies(
            text,
        )

        self.assertEqual(
            actual_counts,
            expected_counts,
        )


if __name__ == "__main__":
    unittest.main()
