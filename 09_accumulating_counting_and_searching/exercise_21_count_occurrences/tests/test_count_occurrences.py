import unittest

from solution import (
    count_occurrences,
)


class CountOccurrencesTests(unittest.TestCase):

    def test_multiple_occurrences(
        self,
    ) -> None:
        elements: list[int] = [1, 2, 2, 3]
        target: int = 2
        expected_occurrences: int = 2

        actual_occurrences: int = count_occurrences(
            elements,
            target,
        )

        self.assertEqual(
            actual_occurrences,
            expected_occurrences,
        )

    def test_empty_list_returns_zero(
        self,
    ) -> None:
        elements: list[int] = []
        target: int = 2
        expected_occurrences: int = 0

        actual_occurrences: int = count_occurrences(
            elements,
            target,
        )

        self.assertEqual(
            actual_occurrences,
            expected_occurrences,
        )


if __name__ == "__main__":
    unittest.main()
