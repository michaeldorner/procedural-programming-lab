import unittest
from typing import cast

from solution import distance


class DistanceCalculationTests(unittest.TestCase):

    def test_distance_between_origin_and_point(
        self,
    ) -> None:
        point_a: tuple[float, float] = (0.0, 0.0)
        point_b: tuple[float, float] = (3.0, 4.0)
        expected_distance: float = 5.0

        actual_distance: float = distance(
            point_a,
            point_b,
        )

        self.assertAlmostEqual(
            actual_distance,
            expected_distance,
        )

    def test_distance_between_identical_points(
        self,
    ) -> None:
        point_a: tuple[float, float] = (1.0, 1.0)
        point_b: tuple[float, float] = (1.0, 1.0)
        expected_distance: float = 0.0

        actual_distance: float = distance(
            point_a,
            point_b,
        )

        self.assertAlmostEqual(
            actual_distance,
            expected_distance,
        )

    def test_distance_with_negative_coordinates(
        self,
    ) -> None:
        point_a: tuple[float, float] = (-1.0, -1.0)
        point_b: tuple[float, float] = (2.0, 3.0)
        expected_distance: float = 5.0

        actual_distance: float = distance(
            point_a,
            point_b,
        )

        self.assertAlmostEqual(
            actual_distance,
            expected_distance,
        )

    def test_distance_with_decimal_coordinates(
        self,
    ) -> None:
        point_a: tuple[float, float] = (1.5, 2.0)
        point_b: tuple[float, float] = (4.5, 6.0)
        expected_distance: float = 5.0

        actual_distance: float = distance(
            point_a,
            point_b,
        )

        self.assertAlmostEqual(
            actual_distance,
            expected_distance,
        )

    def test_distance_symmetry(
        self,
    ) -> None:
        point_a: tuple[float, float] = (1.0, 2.0)
        point_b: tuple[float, float] = (4.0, 6.0)

        distance_forward: float = distance(
            point_a,
            point_b,
        )
        distance_reverse: float = distance(
            point_b,
            point_a,
        )

        self.assertAlmostEqual(
            distance_forward,
            distance_reverse,
        )


class PointValidationTests(unittest.TestCase):

    def test_rejects_point_with_single_coordinate(
        self,
    ) -> None:
        invalid_point: tuple[float, float] = cast(
            tuple[float, float],
            (1.0,),
        )
        valid_point: tuple[float, float] = (3.0, 4.0)

        with self.assertRaises(
            ValueError,
        ):
            distance(
                invalid_point,
                valid_point,
            )

    def test_rejects_point_with_three_coordinates(
        self,
    ) -> None:
        valid_point: tuple[float, float] = (0.0, 0.0)
        invalid_point: tuple[float, float] = cast(
            tuple[float, float],
            (1.0, 2.0, 3.0),
        )

        with self.assertRaises(
            ValueError,
        ):
            distance(
                valid_point,
                invalid_point,
            )

    def test_rejects_nan_coordinate(
        self,
    ) -> None:
        point_with_nan: tuple[float, float] = (float("nan"), 0.0)
        valid_point: tuple[float, float] = (3.0, 4.0)

        with self.assertRaises(
            ValueError,
        ):
            distance(
                point_with_nan,
                valid_point,
            )

    def test_rejects_infinite_coordinate(
        self,
    ) -> None:
        valid_point: tuple[float, float] = (0.0, 0.0)
        point_with_inf: tuple[float, float] = (float("inf"), 4.0)

        with self.assertRaises(
            ValueError,
        ):
            distance(
                valid_point,
                point_with_inf,
            )


if __name__ == "__main__":
    unittest.main()
