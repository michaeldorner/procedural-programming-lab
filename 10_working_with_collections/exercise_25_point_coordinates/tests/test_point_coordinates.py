import unittest

from solution import (
    midpoint,
)


class MidpointCalculationTests(unittest.TestCase):

    def test_positive_coordinates(
        self,
    ) -> None:
        point_a: tuple[float, float] = (0.0, 0.0)
        point_b: tuple[float, float] = (2.0, 4.0)
        expected_midpoint: tuple[float, float] = (1.0, 2.0)

        actual_midpoint: tuple[float, float] = midpoint(
            point_a,
            point_b,
        )

        self.assertEqual(
            actual_midpoint,
            expected_midpoint,
        )

    def test_mixed_sign_coordinates(
        self,
    ) -> None:
        point_a: tuple[float, float] = (-1.0, 1.0)
        point_b: tuple[float, float] = (1.0, 3.0)
        expected_midpoint: tuple[float, float] = (0.0, 2.0)

        actual_midpoint: tuple[float, float] = midpoint(
            point_a,
            point_b,
        )

        self.assertEqual(
            actual_midpoint,
            expected_midpoint,
        )


if __name__ == "__main__":
    unittest.main()
