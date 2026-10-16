import unittest

from datetime import date

from solution import (
    format_date_iso,
    format_date_german,
)


class Exercise64BonusTests(unittest.TestCase):

    def test_format_date_german_1(
        self,
    ) -> None:
        value_0 = date(2026, 7, 14)
        expected_result = '14.07.2026'

        actual_result = format_date_german(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
