"""Unit tests for amortization_schedule."""

import unittest

from amortization_schedule import amortization_schedule, monthly_payment


class TestAmortizationSchedule(unittest.TestCase):
    """Tests for monthly_payment and amortization_schedule."""

    def test_zero_interest_schedule(self) -> None:
        self.assertAlmostEqual(monthly_payment(1200.0, 0.0, 12), 100.0)
        self.assertEqual(
            amortization_schedule(1200.0, 0.0, 2),
            [(1, 600.0, 0.0, 600.0), (2, 600.0, 0.0, 0.0)],
        )

    def test_positive_interest_and_invalid(self) -> None:
        rows = amortization_schedule(1200.0, 0.12, 12)
        self.assertEqual(len(rows), 12)
        self.assertEqual(rows[-1][3], 0.0)
        with self.assertRaises(ValueError):
            amortization_schedule(0.0, 0.05, 12)
