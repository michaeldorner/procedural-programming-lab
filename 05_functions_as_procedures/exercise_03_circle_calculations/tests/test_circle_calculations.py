import math
import unittest

from solution import (
    circle_area,
    circle_circumference,
)


class CircleAreaTests(unittest.TestCase):

    def test_unit_radius(
        self,
    ) -> None:
        radius: float = 1.0
        expected_area: float = math.pi

        actual_area: float = circle_area(
            radius,
        )

        self.assertAlmostEqual(
            actual_area,
            expected_area,
        )

    def test_zero_radius(
        self,
    ) -> None:
        radius: float = 0.0
        expected_area: float = 0.0

        actual_area: float = circle_area(
            radius,
        )

        self.assertEqual(
            actual_area,
            expected_area,
        )

    def test_decimal_radius(
        self,
    ) -> None:
        radius: float = 2.5
        expected_area: float = math.pi * 2.5 * 2.5

        actual_area: float = circle_area(
            radius,
        )

        self.assertAlmostEqual(
            actual_area,
            expected_area,
        )


class CircleCircumferenceTests(unittest.TestCase):

    def test_unit_radius(
        self,
    ) -> None:
        radius: float = 1.0
        expected_circumference: float = 2.0 * math.pi

        actual_circumference: float = circle_circumference(
            radius,
        )

        self.assertAlmostEqual(
            actual_circumference,
            expected_circumference,
        )

    def test_zero_radius(
        self,
    ) -> None:
        radius: float = 0.0
        expected_circumference: float = 0.0

        actual_circumference: float = circle_circumference(
            radius,
        )

        self.assertEqual(
            actual_circumference,
            expected_circumference,
        )

    def test_decimal_radius(
        self,
    ) -> None:
        radius: float = 2.5
        expected_circumference: float = 2.0 * math.pi * 2.5

        actual_circumference: float = circle_circumference(
            radius,
        )

        self.assertAlmostEqual(
            actual_circumference,
            expected_circumference,
        )


class CircleValidationTests(unittest.TestCase):

    def test_area_rejects_negative_radius(
        self,
    ) -> None:
        radius: float = -1.0

        with self.assertRaises(
            ValueError,
        ):
            circle_area(
                radius,
            )

    def test_circumference_rejects_negative_radius(
        self,
    ) -> None:
        radius: float = -1.0

        with self.assertRaises(
            ValueError,
        ):
            circle_circumference(
                radius,
            )

    def test_area_rejects_nan_radius(
        self,
    ) -> None:
        radius: float = float("nan")

        with self.assertRaises(
            ValueError,
        ):
            circle_area(
                radius,
            )

    def test_circumference_rejects_infinite_radius(
        self,
    ) -> None:
        radius: float = float("inf")

        with self.assertRaises(
            ValueError,
        ):
            circle_circumference(
                radius,
            )


class CircleConsistencyTests(unittest.TestCase):

    def test_area_and_circumference_relationship(
        self,
    ) -> None:
        radius: float = 3.0

        calculated_area: float = circle_area(
            radius,
        )
        calculated_circumference: float = circle_circumference(
            radius,
        )
        expected_circumference_squared: float = 4.0 * math.pi * calculated_area
        actual_circumference_squared: float = (
            calculated_circumference * calculated_circumference
        )

        self.assertAlmostEqual(
            actual_circumference_squared,
            expected_circumference_squared,
        )


if __name__ == "__main__":
    unittest.main()
