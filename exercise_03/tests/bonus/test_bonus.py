import math
import unittest

from solution import (
    circle_area,
    circle_circumference,
)


class Exercise03BonusTests(unittest.TestCase):

    def test_circle_area_with_zero_radius(
        self,
    ) -> None:
        radius = 0.0
        expected_area = 0.0

        actual_area = circle_area(
            radius,
        )

        self.assertEqual(
            actual_area,
            expected_area,
        )

    def test_circle_circumference_with_zero_radius(
        self,
    ) -> None:
        radius = 0.0
        expected_circumference = 0.0

        actual_circumference = circle_circumference(
            radius,
        )

        self.assertEqual(
            actual_circumference,
            expected_circumference,
        )

    def test_circle_area_with_decimal_radius(
        self,
    ) -> None:
        radius = 2.5
        expected_area = math.pi * 2.5 * 2.5

        actual_area = circle_area(
            radius,
        )

        self.assertAlmostEqual(
            actual_area,
            expected_area,
        )

    def test_circle_circumference_with_decimal_radius(
        self,
    ) -> None:
        radius = 2.5
        expected_circumference = 2 * math.pi * 2.5

        actual_circumference = circle_circumference(
            radius,
        )

        self.assertAlmostEqual(
            actual_circumference,
            expected_circumference,
        )

    def test_circle_area_with_negative_radius(
        self,
    ) -> None:
        radius = -1.0

        with self.assertRaises(ValueError):
            circle_area(
                radius,
            )

    def test_circle_circumference_with_negative_radius(
        self,
    ) -> None:
        radius = -1.0

        with self.assertRaises(ValueError):
            circle_circumference(
                radius,
            )

    def test_circle_area_with_nan_radius(
        self,
    ) -> None:
        radius = float("nan")

        with self.assertRaises(ValueError):
            circle_area(
                radius,
            )

    def test_circle_circumference_with_infinite_radius(
        self,
    ) -> None:
        radius = float("inf")

        with self.assertRaises(ValueError):
            circle_circumference(
                radius,
            )

    def test_circle_area_and_circumference_are_consistent(
        self,
    ) -> None:
        radius = 3.0

        area = circle_area(
            radius,
        )

        circumference = circle_circumference(
            radius,
        )

        expected_circumference_squared = 4 * math.pi * area
        actual_circumference_squared = circumference * circumference

        self.assertAlmostEqual(
            actual_circumference_squared,
            expected_circumference_squared,
        )


if __name__ == "__main__":
    unittest.main()
