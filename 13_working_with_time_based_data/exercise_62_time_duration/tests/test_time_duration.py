import unittest
from datetime import time

from solution import (
    minutes_between,
)


class MinutesBetweenTests(unittest.TestCase):

    def test_same_day_interval(
        self,
    ) -> None:
        start_time: time = time(10, 0)
        end_time: time = time(11, 30)
        expected_minutes: int = 90

        actual_minutes: int = minutes_between(
            start_time,
            end_time,
        )

        self.assertEqual(
            actual_minutes,
            expected_minutes,
        )

    def test_zero_minute_interval(
        self,
    ) -> None:
        start_time: time = time(10, 0)
        end_time: time = time(10, 0)
        expected_minutes: int = 0

        actual_minutes: int = minutes_between(
            start_time,
            end_time,
        )

        self.assertEqual(
            actual_minutes,
            expected_minutes,
        )


if __name__ == "__main__":
    unittest.main()
