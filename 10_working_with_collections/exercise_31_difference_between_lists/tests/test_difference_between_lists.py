import unittest

from solution import (
    difference,
)


class ListDifferenceTests(unittest.TestCase):

    def test_non_empty_difference(
        self,
    ) -> None:
        first_list: list[int] = [1, 2, 3]
        second_list: list[int] = [2, 4]
        expected_difference: set[int] = {1, 3}

        actual_difference: set[int] = difference(
            first_list,
            second_list,
        )

        self.assertEqual(
            actual_difference,
            expected_difference,
        )

    def test_empty_first_list(
        self,
    ) -> None:
        first_list: list[int] = []
        second_list: list[int] = [1]
        expected_difference: set[int] = set()

        actual_difference: set[int] = difference(
            first_list,
            second_list,
        )

        self.assertEqual(
            actual_difference,
            expected_difference,
        )


if __name__ == "__main__":
    unittest.main()
