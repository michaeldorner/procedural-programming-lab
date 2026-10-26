import unittest

from solution import (
    unique_values,
)


class UniqueValuesTests(unittest.TestCase):

    def test_list_with_duplicates(
        self,
    ) -> None:
        numbers: list[int] = [1, 2, 1, 3]
        expected_set: set[int] = {1, 2, 3}

        actual_set: set[int] = unique_values(
            numbers,
        )

        self.assertEqual(
            actual_set,
            expected_set,
        )

    def test_empty_list(
        self,
    ) -> None:
        numbers: list[int] = []
        expected_set: set[int] = set()

        actual_set: set[int] = unique_values(
            numbers,
        )

        self.assertEqual(
            actual_set,
            expected_set,
        )


if __name__ == "__main__":
    unittest.main()
