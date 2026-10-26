import unittest

from solution import (
    expense_total,
)


class ExpenseTotalTests(unittest.TestCase):

    def test_multiple_expenses_total(
        self,
    ) -> None:
        expense_records: list[dict[str, float]] = [{"amount": 2.5}, {"amount": 3.5}]
        expected_total: float = 6.0

        actual_total: float = expense_total(
            expense_records,
        )

        self.assertAlmostEqual(
            actual_total,
            expected_total,
        )

    def test_empty_expenses_list_returns_zero(
        self,
    ) -> None:
        expense_records: list[dict[str, float]] = []
        expected_total: float = 0.0

        actual_total: float = expense_total(
            expense_records,
        )

        self.assertAlmostEqual(
            actual_total,
            expected_total,
        )


if __name__ == "__main__":
    unittest.main()
