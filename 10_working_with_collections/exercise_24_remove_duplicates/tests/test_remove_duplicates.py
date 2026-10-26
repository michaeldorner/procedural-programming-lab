import unittest

from solution import (
    remove_duplicates,
)


class RemoveDuplicatesTests(unittest.TestCase):

    def test_preserves_first_occurrence_order(
        self,
    ) -> None:
        numbers: list[int] = [1, 2, 1, 3, 2]
        expected_unique: list[int] = [1, 2, 3]

        actual_unique: list[int] = remove_duplicates(
            numbers,
        )

        self.assertEqual(
            actual_unique,
            expected_unique,
        )

    def test_empty_list_returns_empty(
        self,
    ) -> None:
        numbers: list[int] = []
        expected_unique: list[int] = []

        actual_unique: list[int] = remove_duplicates(
            numbers,
        )

        self.assertEqual(
            actual_unique,
            expected_unique,
        )


if __name__ == "__main__":
    unittest.main()
