import unittest
from datetime import date

from solution import (
    days_between,
)


class DaysBetweenDatesTests(unittest.TestCase):

    def test_distinct_dates_interval(
        self,
    ) -> None:
        start_date: date = date(2026, 1, 1)
        end_date: date = date(2026, 1, 10)
        expected_days: int = 9

        actual_days: int = days_between(
            start_date,
            end_date,
        )

        self.assertEqual(
            actual_days,
            expected_days,
        )

    def test_same_date_returns_zero(
        self,
    ) -> None:
        start_date: date = date(2026, 1, 1)
        end_date: date = date(2026, 1, 1)
        expected_days: int = 0

        actual_days: int = days_between(
            start_date,
            end_date,
        )

        self.assertEqual(
            actual_days,
            expected_days,
        )


if __name__ == "__main__":
    unittest.main()
