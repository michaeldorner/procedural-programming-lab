import unittest
from typing import cast

from solution import triangle_type


class TriangleClassificationTests(unittest.TestCase):

    def test_equilateral_triangle(
        self,
    ) -> None:
        side_a: float = 3.0
        side_b: float = 3.0
        side_c: float = 3.0
        expected_type: str = "equilateral"

        actual_type: str = triangle_type(
            side_a,
            side_b,
            side_c,
        )

        self.assertEqual(
            actual_type,
            expected_type,
        )

    def test_isosceles_triangle(
        self,
    ) -> None:
        side_a: float = 3.0
        side_b: float = 3.0
        side_c: float = 4.0
        expected_type: str = "isosceles"

        actual_type: str = triangle_type(
            side_a,
            side_b,
            side_c,
        )

        self.assertEqual(
            actual_type,
            expected_type,
        )

    def test_scalene_triangle(
        self,
    ) -> None:
        side_a: float = 3.0
        side_b: float = 4.0
        side_c: float = 5.0
        expected_type: str = "scalene"

        actual_type: str = triangle_type(
            side_a,
            side_b,
            side_c,
        )

        self.assertEqual(
            actual_type,
            expected_type,
        )

    def test_degenerate_triangle_is_invalid(
        self,
    ) -> None:
        side_a: float = 1.0
        side_b: float = 2.0
        side_c: float = 3.0
        expected_type: str = "invalid"

        actual_type: str = triangle_type(
            side_a,
            side_b,
            side_c,
        )

        self.assertEqual(
            actual_type,
            expected_type,
        )

    def test_triangle_inequality_violation_is_invalid(
        self,
    ) -> None:
        side_a: float = 1.0
        side_b: float = 2.0
        side_c: float = 5.0
        expected_type: str = "invalid"

        actual_type: str = triangle_type(
            side_a,
            side_b,
            side_c,
        )

        self.assertEqual(
            actual_type,
            expected_type,
        )


class TriangleValidationTests(unittest.TestCase):

    def test_rejects_zero_side_length(
        self,
    ) -> None:
        side_a: float = 0.0
        side_b: float = 3.0
        side_c: float = 4.0

        with self.assertRaises(
            ValueError,
        ):
            triangle_type(
                side_a,
                side_b,
                side_c,
            )

    def test_rejects_negative_side_length(
        self,
    ) -> None:
        side_a: float = -1.0
        side_b: float = 3.0
        side_c: float = 4.0

        with self.assertRaises(
            ValueError,
        ):
            triangle_type(
                side_a,
                side_b,
                side_c,
            )

    def test_rejects_nan_side_length(
        self,
    ) -> None:
        side_a: float = float("nan")
        side_b: float = 3.0
        side_c: float = 4.0

        with self.assertRaises(
            ValueError,
        ):
            triangle_type(
                side_a,
                side_b,
                side_c,
            )

    def test_rejects_infinite_side_length(
        self,
    ) -> None:
        side_a: float = float("inf")
        side_b: float = 3.0
        side_c: float = 4.0

        with self.assertRaises(
            ValueError,
        ):
            triangle_type(
                side_a,
                side_b,
                side_c,
            )


if __name__ == "__main__":
    unittest.main()
