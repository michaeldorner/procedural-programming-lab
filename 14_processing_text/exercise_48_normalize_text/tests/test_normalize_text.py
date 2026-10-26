import unittest

from solution import (
    normalize_text,
)


class NormalizeTextTests(unittest.TestCase):

    def test_strips_padding_and_converts_case(
        self,
    ) -> None:
        raw_text: str = "  Hello  "
        expected_text: str = "hello"

        actual_text: str = normalize_text(
            raw_text,
        )

        self.assertEqual(
            actual_text,
            expected_text,
        )

    def test_uppercase_word(
        self,
    ) -> None:
        raw_text: str = "PYTHON"
        expected_text: str = "python"

        actual_text: str = normalize_text(
            raw_text,
        )

        self.assertEqual(
            actual_text,
            expected_text,
        )


if __name__ == "__main__":
    unittest.main()
