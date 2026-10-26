import unittest
from typing import cast

from solution import is_leap_year


class LeapYearTests(unittest.TestCase):

    def test_typical_leap_year_divisible_by_four(
        self,
    ) -> None:
        year: int = 2024

        leap_result: bool = is_leap_year(
            year,
        )

        self.assertTrue(
            leap_result,
        )

    def test_typical_common_year(
        self,
    ) -> None:
        year: int = 2023

        leap_result: bool = is_leap_year(
            year,
        )

        self.assertFalse(
            leap_result,
        )

    def test_century_not_divisible_by_four_hundred_is_common(
        self,
    ) -> None:
        year: int = 1900

        leap_result: bool = is_leap_year(
            year,
        )

        self.assertFalse(
            leap_result,
        )

    def test_century_divisible_by_four_hundred_is_leap(
        self,
    ) -> None:
        year: int = 2000

        leap_result: bool = is_leap_year(
            year,
        )

        self.assertTrue(
            leap_result,
        )

    def test_year_four_is_leap(
        self,
    ) -> None:
        year: int = 4

        leap_result: bool = is_leap_year(
            year,
        )

        self.assertTrue(
            leap_result,
        )

    def test_year_one_is_common(
        self,
    ) -> None:
        year: int = 1

        leap_result: bool = is_leap_year(
            year,
        )

        self.assertFalse(
            leap_result,
        )


class YearValidationTests(unittest.TestCase):

    def test_rejects_year_zero(
        self,
    ) -> None:
        year: int = 0

        with self.assertRaises(
            ValueError,
        ):
            is_leap_year(
                year,
            )

    def test_rejects_negative_year(
        self,
    ) -> None:
        year: int = -4

        with self.assertRaises(
            ValueError,
        ):
            is_leap_year(
                year,
            )

    def test_rejects_boolean_true(
        self,
    ) -> None:
        boolean_year: int = cast(
            int,
            True,
        )

        with self.assertRaises(
            ValueError,
        ):
            is_leap_year(
                boolean_year,
            )

    def test_rejects_boolean_false(
        self,
    ) -> None:
        boolean_year: int = cast(
            int,
            False,
        )

        with self.assertRaises(
            ValueError,
        ):
            is_leap_year(
                boolean_year,
            )

    def test_rejects_float_year(
        self,
    ) -> None:
        float_year: int = cast(
            int,
            2024.0,
        )

        with self.assertRaises(
            ValueError,
        ):
            is_leap_year(
                float_year,
            )


if __name__ == "__main__":
    unittest.main()
