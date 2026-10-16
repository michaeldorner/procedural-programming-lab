import unittest
from typing import cast

from solution import is_even


class Exercise06BonusTests(unittest.TestCase):

    def test_zero_is_even(
        self,
    ) -> None:
        number: int = 0
        expected_result: bool = True

        actual_result: bool = is_even(
            number,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_negative_even_number(
        self,
    ) -> None:
        number: int = -2
        expected_result: bool = True

        actual_result: bool = is_even(
            number,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_negative_odd_number(
        self,
    ) -> None:
        number: int = -3
        expected_result: bool = False

        actual_result: bool = is_even(
            number,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_large_even_number(
        self,
    ) -> None:
        number: int = 1_000_000
        expected_result: bool = True

        actual_result: bool = is_even(
            number,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_boolean_true_is_rejected(
        self,
    ) -> None:
        number = cast(
            int,
            True,
        )

        with self.assertRaises(ValueError):
            is_even(
                number,
            )

    def test_boolean_false_is_rejected(
        self,
    ) -> None:
        number = cast(
            int,
            False,
        )

        with self.assertRaises(ValueError):
            is_even(
                number,
            )

    def test_float_is_rejected(
        self,
    ) -> None:
        number = cast(
            int,
            2.0,
        )

        with self.assertRaises(ValueError):
            is_even(
                number,
            )


if __name__ == "__main__":
    unittest.main()
