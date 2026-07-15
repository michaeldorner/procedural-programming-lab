import unittest

from solution import distance


class Exercise04RequiredTests(unittest.TestCase):

    def test_distance_between_origin_and_point(
        self,
    ) -> None:
        point_a: tuple[float, float] = (
            0.0,
            0.0,
        )
        point_b: tuple[float, float] = (
            3.0,
            4.0,
        )
        expected_distance = 5.0

        actual_distance = distance(
            point_a,
            point_b,
        )

        self.assertEqual(
            actual_distance,
            expected_distance,
        )

    def test_distance_between_same_point(
        self,
    ) -> None:
        point_a: tuple[float, float] = (
            1.0,
            1.0,
        )
        point_b: tuple[float, float] = (
            1.0,
            1.0,
        )
        expected_distance = 0.0

        actual_distance = distance(
            point_a,
            point_b,
        )

        self.assertEqual(
            actual_distance,
            expected_distance,
        )


if __name__ == "__main__":
    unittest.main()
