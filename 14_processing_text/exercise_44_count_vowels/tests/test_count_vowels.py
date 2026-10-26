import unittest

from solution import (
    count_vowels,
)


class CountVowelsTests(unittest.TestCase):

    def test_lowercase_word(
        self,
    ) -> None:
        sample_text: str = "hello"
        expected_vowel_count: int = 2

        actual_vowel_count: int = count_vowels(
            sample_text,
        )

        self.assertEqual(
            actual_vowel_count,
            expected_vowel_count,
        )

    def test_all_uppercase_vowels(
        self,
    ) -> None:
        sample_text: str = "AEIOU"
        expected_vowel_count: int = 5

        actual_vowel_count: int = count_vowels(
            sample_text,
        )

        self.assertEqual(
            actual_vowel_count,
            expected_vowel_count,
        )


if __name__ == "__main__":
    unittest.main()
