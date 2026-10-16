import unittest

from datetime import date

from solution import (
    is_overdue,
)


class Exercise63BonusTests(unittest.TestCase):

    def test_is_overdue_1(
        self,
    ) -> None:
        value_0 = date(2026, 1, 1)
        value_1 = date(2026, 1, 1)
        expected_result = False

        actual_result = is_overdue(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
