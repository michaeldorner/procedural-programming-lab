import unittest

from solution import (
    count_first_quadrant,
)


class FirstQuadrantPointsTests(unittest.TestCase):

    def test_mixed_quadrant_points(
        self,
    ) -> None:
        points: list[tuple[float, float]] = [(1.0, 2.0), (-1.0, 3.0), (4.0, 5.0)]
        expected_count: int = 2

        actual_count: int = count_first_quadrant(
            points,
        )

        self.assertEqual(
            actual_count,
            expected_count,
        )

    def test_axis_points_not_in_first_quadrant(
        self,
    ) -> None:
        points: list[tuple[float, float]] = [(0.0, 1.0), (1.0, 0.0)]
        expected_count: int = 0

        actual_count: int = count_first_quadrant(
            points,
        )

        self.assertEqual(
            actual_count,
            expected_count,
        )


if __name__ == "__main__":
    unittest.main()
