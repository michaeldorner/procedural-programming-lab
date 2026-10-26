import unittest

from solution import (
    TrafficLight,
    can_cross,
)


class TrafficLightCrossingTests(unittest.TestCase):

    def test_green_light_allows_crossing(
        self,
    ) -> None:
        signal: TrafficLight = TrafficLight.GREEN

        pedestrian_allowed: bool = can_cross(
            signal,
        )

        self.assertTrue(
            pedestrian_allowed,
        )

    def test_red_light_prohibits_crossing(
        self,
    ) -> None:
        signal: TrafficLight = TrafficLight.RED

        pedestrian_allowed: bool = can_cross(
            signal,
        )

        self.assertFalse(
            pedestrian_allowed,
        )

    def test_yellow_light_prohibits_crossing(
        self,
    ) -> None:
        signal: TrafficLight = TrafficLight.YELLOW

        pedestrian_allowed: bool = can_cross(
            signal,
        )

        self.assertFalse(
            pedestrian_allowed,
        )


if __name__ == "__main__":
    unittest.main()
