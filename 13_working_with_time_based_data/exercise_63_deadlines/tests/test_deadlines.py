import unittest
from datetime import date

from solution import (
    is_overdue,
)


class DeadlineOverdueTests(unittest.TestCase):

    def test_current_date_after_due_date_is_overdue(
        self,
    ) -> None:
        due_date: date = date(2026, 1, 1)
        current_date: date = date(2026, 1, 2)

        overdue_status: bool = is_overdue(
            due_date,
            current_date,
        )

        self.assertTrue(
            overdue_status,
        )

    def test_current_date_before_due_date_is_not_overdue(
        self,
    ) -> None:
        due_date: date = date(2026, 1, 2)
        current_date: date = date(2026, 1, 1)

        overdue_status: bool = is_overdue(
            due_date,
            current_date,
        )

        self.assertFalse(
            overdue_status,
        )


if __name__ == "__main__":
    unittest.main()
