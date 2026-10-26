import unittest

from solution import (
    word_count,
)


class WordCountTests(unittest.TestCase):

    def test_simple_two_word_sentence(
        self,
    ) -> None:
        text: str = "hello world"
        expected_count: int = 2

        actual_count: int = word_count(
            text,
        )

        self.assertEqual(
            actual_count,
            expected_count,
        )

    def test_multiple_spaces_and_padding(
        self,
    ) -> None:
        text: str = "  many   spaces  "
        expected_count: int = 2

        actual_count: int = word_count(
            text,
        )

        self.assertEqual(
            actual_count,
            expected_count,
        )


if __name__ == "__main__":
    unittest.main()
