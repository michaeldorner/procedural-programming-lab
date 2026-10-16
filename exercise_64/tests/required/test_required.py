import unittest

from datetime import date

from solution import (
    format_date_iso,
    format_date_german,
)


class Exercise64RequiredTests(unittest.TestCase):

    def test_format_date_iso_1(
        self,
    ) -> None:
        value_0 = date(2026, 7, 14)
        expected_result = '2026-07-14'

        actual_result = format_date_iso(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
