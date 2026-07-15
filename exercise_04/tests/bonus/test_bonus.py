import unittest
from typing import cast

from solution import distance


class Exercise04BonusTests(unittest.TestCase):

    def test_distance_with_negative_coordinates(
        self,
    ) -> None:
        point_a: tuple[float, float] = (
            -1.0,
            -1.0,
        )
        point_b: tuple[float, float] = (
            2.0,
            3.0,
        )
        expected_distance: float = 5.0

        actual_distance: float = distance(
            point_a,
            point_b,
        )

        self.assertAlmostEqual(
            actual_distance,
            expected_distance,
        )

    def test_distance_is_symmetric(
        self,
    ) -> None:
        point_a: tuple[float, float] = (
            1.0,
            2.0,
        )
        point_b: tuple[float, float] = (
            4.0,
            6.0,
        )

        distance_ab: float = distance(
            point_a,
            point_b,
        )

        distance_ba: float = distance(
            point_b,
            point_a,
        )

        self.assertAlmostEqual(
            distance_ab,
            distance_ba,
        )

    def test_distance_with_decimal_coordinates(
        self,
    ) -> None:
        point_a: tuple[float, float] = (
            1.5,
            2.0,
        )
        point_b: tuple[float, float] = (
            4.5,
            6.0,
        )
        expected_distance: float = 5.0

        actual_distance: float = distance(
            point_a,
            point_b,
        )

        self.assertAlmostEqual(
            actual_distance,
            expected_distance,
        )

    def test_distance_with_invalid_first_point(
        self,
    ) -> None:
        point_a = cast(
            tuple[float, float],
            (
                1.0,
            ),
        )
        point_b: tuple[float, float] = (
            3.0,
            4.0,
        )

        with self.assertRaises(ValueError):
            distance(
                point_a,
                point_b,
            )

    def test_distance_with_invalid_second_point(
        self,
    ) -> None:
        point_a: tuple[float, float] = (
            0.0,
            0.0,
        )
        point_b = cast(
            tuple[float, float],
            (
                1.0,
                2.0,
                3.0,
            ),
        )

        with self.assertRaises(ValueError):
            distance(
                point_a,
                point_b,
            )

    def test_distance_with_nan_coordinate(
        self,
    ) -> None:
        point_a: tuple[float, float] = (
            float("nan"),
            0.0,
        )
        point_b: tuple[float, float] = (
            3.0,
            4.0,
        )

        with self.assertRaises(ValueError):
            distance(
                point_a,
                point_b,
            )

    def test_distance_with_infinite_coordinate(
        self,
    ) -> None:
        point_a: tuple[float, float] = (
            0.0,
            0.0,
        )
        point_b: tuple[float, float] = (
            float("inf"),
            4.0,
        )

        with self.assertRaises(ValueError):
            distance(
                point_a,
                point_b,
            )


if __name__ == "__main__":
    unittest.main()
