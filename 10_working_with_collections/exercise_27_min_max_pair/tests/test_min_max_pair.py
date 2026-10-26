import unittest

from solution import (
    min_max,
)


class MinMaxPairTests(unittest.TestCase):

    def test_positive_integers(
        self,
    ) -> None:
        numbers: list[int] = [3, 1, 4]
        expected_bounds: tuple[int, int] = (1, 4)

        actual_bounds: tuple[int, int] = min_max(
            numbers,
        )

        self.assertEqual(
            actual_bounds,
            expected_bounds,
        )

    def test_negative_integers(
        self,
    ) -> None:
        numbers: list[int] = [-3, -1, -4]
        expected_bounds: tuple[int, int] = (-4, -1)

        actual_bounds: tuple[int, int] = min_max(
            numbers,
        )

        self.assertEqual(
            actual_bounds,
            expected_bounds,
        )


if __name__ == "__main__":
    unittest.main()
