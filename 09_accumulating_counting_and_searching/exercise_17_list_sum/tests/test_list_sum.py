import unittest

from solution import (
    list_sum,
)


class ListSumCalculationTests(unittest.TestCase):

    def test_positive_integers(
        self,
    ) -> None:
        numbers: list[int] = [1, 2, 3]
        expected_sum: int = 6

        actual_sum: int = list_sum(
            numbers,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )


class EmptyListSumTests(unittest.TestCase):

    def test_empty_list_sum_is_zero(
        self,
    ) -> None:
        numbers: list[int] = []
        expected_sum: int = 0

        actual_sum: int = list_sum(
            numbers,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )


if __name__ == "__main__":
    unittest.main()
