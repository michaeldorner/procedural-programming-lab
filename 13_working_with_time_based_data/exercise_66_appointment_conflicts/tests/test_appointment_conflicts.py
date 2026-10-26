import unittest
from datetime import datetime

from solution import (
    appointments_overlap,
)


class AppointmentOverlapTests(unittest.TestCase):

    def test_overlapping_intervals(
        self,
    ) -> None:
        start_a: datetime = datetime(2026, 1, 1, 10, 0)
        end_a: datetime = datetime(2026, 1, 1, 11, 0)
        start_b: datetime = datetime(2026, 1, 1, 10, 30)
        end_b: datetime = datetime(2026, 1, 1, 11, 30)

        conflict: bool = appointments_overlap(
            start_a,
            end_a,
            start_b,
            end_b,
        )

        self.assertTrue(
            conflict,
        )

    def test_adjacent_intervals_do_not_overlap(
        self,
    ) -> None:
        start_a: datetime = datetime(2026, 1, 1, 10, 0)
        end_a: datetime = datetime(2026, 1, 1, 11, 0)
        start_b: datetime = datetime(2026, 1, 1, 11, 0)
        end_b: datetime = datetime(2026, 1, 1, 12, 0)

        conflict: bool = appointments_overlap(
            start_a,
            end_a,
            start_b,
            end_b,
        )

        self.assertFalse(
            conflict,
        )


if __name__ == "__main__":
    unittest.main()
