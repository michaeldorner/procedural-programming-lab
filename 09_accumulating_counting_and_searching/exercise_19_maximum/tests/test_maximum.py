import unittest

from solution import (
    maximum,
)


class ListMaximumTests(unittest.TestCase):

    def test_positive_integers(
        self,
    ) -> None:
        values: list[int] = [1, 5, 3]
        expected_maximum: int = 5

        actual_maximum: int = maximum(
            values,
        )

        self.assertEqual(
            actual_maximum,
            expected_maximum,
        )

    def test_negative_integers(
        self,
    ) -> None:
        values: list[int] = [-5, -2, -9]
        expected_maximum: int = -2

        actual_maximum: int = maximum(
            values,
        )

        self.assertEqual(
            actual_maximum,
            expected_maximum,
        )


if __name__ == "__main__":
    unittest.main()
