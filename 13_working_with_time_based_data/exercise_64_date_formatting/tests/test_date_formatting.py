import unittest
from datetime import date

from solution import (
    format_date_german,
    format_date_iso,
)


class DateFormattingTests(unittest.TestCase):

    def test_iso_format(
        self,
    ) -> None:
        target_date: date = date(2026, 1, 5)
        expected_iso: str = "2026-01-05"

        actual_iso: str = format_date_iso(
            target_date,
        )

        self.assertEqual(
            actual_iso,
            expected_iso,
        )

    def test_german_format(
        self,
    ) -> None:
        target_date: date = date(2026, 1, 5)
        expected_german: str = "05.01.2026"

        actual_german: str = format_date_german(
            target_date,
        )

        self.assertEqual(
            actual_german,
            expected_german,
        )


if __name__ == "__main__":
    unittest.main()
