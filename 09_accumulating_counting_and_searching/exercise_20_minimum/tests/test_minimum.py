import unittest

from solution import (
    minimum,
)


class ListMinimumTests(unittest.TestCase):

    def test_positive_integers(
        self,
    ) -> None:
        values: list[int] = [1, 5, 3]
        expected_minimum: int = 1

        actual_minimum: int = minimum(
            values,
        )

        self.assertEqual(
            actual_minimum,
            expected_minimum,
        )

    def test_negative_integers(
        self,
    ) -> None:
        values: list[int] = [-5, -2, -9]
        expected_minimum: int = -9

        actual_minimum: int = minimum(
            values,
        )

        self.assertEqual(
            actual_minimum,
            expected_minimum,
        )


if __name__ == "__main__":
    unittest.main()
