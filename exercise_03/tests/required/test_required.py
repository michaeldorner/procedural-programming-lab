import math
import unittest

from solution import (
    circle_area,
    circle_circumference,
)


class Exercise03RequiredTests(unittest.TestCase):

    def test_circle_area_with_radius_one(
        self,
    ) -> None:
        radius = 1.0
        expected_area = math.pi

        actual_area = circle_area(
            radius,
        )

        self.assertAlmostEqual(
            actual_area,
            expected_area,
        )

    def test_circle_circumference_with_radius_one(
        self,
    ) -> None:
        radius = 1.0
        expected_circumference = 2 * math.pi

        actual_circumference = circle_circumference(
            radius,
        )

        self.assertAlmostEqual(
            actual_circumference,
            expected_circumference,
        )


if __name__ == "__main__":
    unittest.main()
