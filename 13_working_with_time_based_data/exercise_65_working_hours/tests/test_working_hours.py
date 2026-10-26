import unittest
from datetime import time

from solution import (
    is_working_hour,
)


class WorkingHoursTests(unittest.TestCase):

    def test_mid_morning_is_working_hour(
        self,
    ) -> None:
        check_time: time = time(10, 0)

        within_hours: bool = is_working_hour(
            check_time,
        )

        self.assertTrue(
            within_hours,
        )

    def test_early_morning_is_not_working_hour(
        self,
    ) -> None:
        check_time: time = time(8, 0)

        within_hours: bool = is_working_hour(
            check_time,
        )

        self.assertFalse(
            within_hours,
        )


if __name__ == "__main__":
    unittest.main()
