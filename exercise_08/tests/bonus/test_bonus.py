import unittest
from typing import cast

from solution import is_leap_year


class Exercise08BonusTests(unittest.TestCase):

    def test_century_year_not_divisible_by_four_hundred(
        self,
    ) -> None:
        year: int = 1900
        expected_result: bool = False

        actual_result: bool = is_leap_year(
            year,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_century_year_divisible_by_four_hundred(
        self,
    ) -> None:
        year: int = 2000
        expected_result: bool = True

        actual_result: bool = is_leap_year(
            year,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_year_divisible_by_one_hundred_but_not_four_hundred(
        self,
    ) -> None:
        year: int = 2100
        expected_result: bool = False

        actual_result: bool = is_leap_year(
            year,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_year_divisible_by_four_but_not_one_hundred(
        self,
    ) -> None:
        year: int = 2028
        expected_result: bool = True

        actual_result: bool = is_leap_year(
            year,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_year_one_is_valid(
        self,
    ) -> None:
        year: int = 1
        expected_result: bool = False

        actual_result: bool = is_leap_year(
            year,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_year_zero_is_rejected(
        self,
    ) -> None:
        year: int = 0

        with self.assertRaises(ValueError):
            is_leap_year(
                year,
            )

    def test_negative_year_is_rejected(
        self,
    ) -> None:
        year: int = -400

        with self.assertRaises(ValueError):
            is_leap_year(
                year,
            )

    def test_boolean_true_is_rejected(
        self,
    ) -> None:
        year = cast(
            int,
            True,
        )

        with self.assertRaises(ValueError):
            is_leap_year(
                year,
            )

    def test_boolean_false_is_rejected(
        self,
    ) -> None:
        year = cast(
            int,
            False,
        )

        with self.assertRaises(ValueError):
            is_leap_year(
                year,
            )

    def test_float_is_rejected(
        self,
    ) -> None:
        year = cast(
            int,
            2024.0,
        )

        with self.assertRaises(ValueError):
            is_leap_year(
                year,
            )


if __name__ == "__main__":
    unittest.main()
