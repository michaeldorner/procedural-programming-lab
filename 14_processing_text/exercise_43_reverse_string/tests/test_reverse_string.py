import unittest

from solution import (
    reverse_string,
)


class ReverseStringTests(unittest.TestCase):

    def test_standard_ascii_string(
        self,
    ) -> None:
        source_text: str = "abc"
        expected_reversed: str = "cba"

        actual_reversed: str = reverse_string(
            source_text,
        )

        self.assertEqual(
            actual_reversed,
            expected_reversed,
        )

    def test_empty_string(
        self,
    ) -> None:
        source_text: str = ""
        expected_reversed: str = ""

        actual_reversed: str = reverse_string(
            source_text,
        )

        self.assertEqual(
            actual_reversed,
            expected_reversed,
        )


if __name__ == "__main__":
    unittest.main()
