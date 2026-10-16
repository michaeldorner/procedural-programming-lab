import unittest
from typing import cast

from solution import triangle_type


class Exercise10BonusTests(unittest.TestCase):

    def test_invalid_triangle_with_degenerate_sides(
        self,
    ) -> None:
        a: float = 1.0
        b: float = 2.0
        c: float = 3.0
        expected_result: str = "invalid"

        actual_result: str = triangle_type(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_invalid_triangle_with_too_long_side(
        self,
    ) -> None:
        a: float = 10.0
        b: float = 2.0
        c: float = 3.0
        expected_result: str = "invalid"

        actual_result: str = triangle_type(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_isosceles_triangle_with_different_equal_sides(
        self,
    ) -> None:
        a: float = 5.0
        b: float = 3.0
        c: float = 5.0
        expected_result: str = "isosceles"

        actual_result: str = triangle_type(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_decimal_side_lengths(
        self,
    ) -> None:
        a: float = 2.5
        b: float = 2.5
        c: float = 3.0
        expected_result: str = "isosceles"

        actual_result: str = triangle_type(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_zero_side_is_rejected(
        self,
    ) -> None:
        a: float = 0.0
        b: float = 3.0
        c: float = 4.0

        with self.assertRaises(ValueError):
            triangle_type(
                a,
                b,
                c,
            )

    def test_negative_side_is_rejected(
        self,
    ) -> None:
        a: float = -1.0
        b: float = 3.0
        c: float = 4.0

        with self.assertRaises(ValueError):
            triangle_type(
                a,
                b,
                c,
            )

    def test_nan_side_is_rejected(
        self,
    ) -> None:
        a: float = float("nan")
        b: float = 3.0
        c: float = 4.0

        with self.assertRaises(ValueError):
            triangle_type(
                a,
                b,
                c,
            )

    def test_infinite_side_is_rejected(
        self,
    ) -> None:
        a: float = float("inf")
        b: float = 3.0
        c: float = 4.0

        with self.assertRaises(ValueError):
            triangle_type(
                a,
                b,
                c,
            )

    def test_string_side_is_rejected(
        self,
    ) -> None:
        a = cast(
            float,
            "3.0",
        )
        b: float = 3.0
        c: float = 4.0

        with self.assertRaises(ValueError):
            triangle_type(
                a,
                b,
                c,
            )

    def test_boolean_side_is_rejected(
        self,
    ) -> None:
        a = cast(
            float,
            True,
        )
        b: float = 3.0
        c: float = 4.0

        with self.assertRaises(ValueError):
            triangle_type(
                a,
                b,
                c,
            )


if __name__ == "__main__":
    unittest.main()
