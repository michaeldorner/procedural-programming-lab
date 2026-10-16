import unittest

from datetime import date

from solution import (
    days_between,
)


class Exercise61RequiredTests(unittest.TestCase):

    def test_days_between_1(
        self,
    ) -> None:
        value_0 = date(2026, 1, 1)
        value_1 = date(2026, 1, 10)
        expected_result = 9

        actual_result = days_between(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
