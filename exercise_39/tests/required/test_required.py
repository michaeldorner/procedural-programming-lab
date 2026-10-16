import unittest

from solution import (
    TrafficLight,
    can_cross,
)


class Exercise39RequiredTests(unittest.TestCase):

    def test_can_cross_1(
        self,
    ) -> None:
        value_0 = TrafficLight.GREEN
        expected_result = True

        actual_result = can_cross(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_can_cross_2(
        self,
    ) -> None:
        value_0 = TrafficLight.RED
        expected_result = False

        actual_result = can_cross(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
