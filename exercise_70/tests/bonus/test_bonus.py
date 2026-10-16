import unittest

from solution import (
    expense_total,
)


class Exercise70BonusTests(unittest.TestCase):

    def test_expense_total_1(
        self,
    ) -> None:
        value_0 = []
        expected_result = 0.0

        actual_result = expense_total(
            value_0,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
