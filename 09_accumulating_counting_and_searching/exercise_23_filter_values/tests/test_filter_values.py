import unittest

from solution import (
    filter_even,
)


class FilterEvenTests(unittest.TestCase):

    def test_mixed_positive_integers(
        self,
    ) -> None:
        numbers: list[int] = [1, 2, 3, 4]
        expected_evens: list[int] = [2, 4]

        actual_evens: list[int] = filter_even(
            numbers,
        )

        self.assertEqual(
            actual_evens,
            expected_evens,
        )

    def test_negative_numbers_and_zero(
        self,
    ) -> None:
        numbers: list[int] = [-2, -1, 0]
        expected_evens: list[int] = [-2, 0]

        actual_evens: list[int] = filter_even(
            numbers,
        )

        self.assertEqual(
            actual_evens,
            expected_evens,
        )


if __name__ == "__main__":
    unittest.main()
