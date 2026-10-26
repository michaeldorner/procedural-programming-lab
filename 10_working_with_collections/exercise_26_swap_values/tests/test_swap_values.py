import unittest

from solution import (
    swap_values,
)


class SwapValuesTests(unittest.TestCase):

    def test_positive_integers(
        self,
    ) -> None:
        first: int = 1
        second: int = 2
        expected_swapped: tuple[int, int] = (2, 1)

        actual_swapped: tuple[int, int] = swap_values(
            first,
            second,
        )

        self.assertEqual(
            actual_swapped,
            expected_swapped,
        )

    def test_mixed_sign_integers(
        self,
    ) -> None:
        first: int = -1
        second: int = 5
        expected_swapped: tuple[int, int] = (5, -1)

        actual_swapped: tuple[int, int] = swap_values(
            first,
            second,
        )

        self.assertEqual(
            actual_swapped,
            expected_swapped,
        )


if __name__ == "__main__":
    unittest.main()
