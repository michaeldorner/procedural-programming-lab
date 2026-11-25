"""Unit tests for build_amortization_schedule."""

import unittest

from .amortization_schedule import build_amortization_schedule, calculate_monthly_payment


class TestAmortizationSchedule(unittest.TestCase):
    """Tests for calculate_monthly_payment and build_amortization_schedule."""

    def test_zero_interest_schedule(self) -> None:
        self.assertAlmostEqual(calculate_monthly_payment(1200.0, 0.0, 12), 100.0)
        self.assertEqual(
            build_amortization_schedule(1200.0, 0.0, 2),
            [(1, 600.0, 0.0, 600.0), (2, 600.0, 0.0, 0.0)],
        )

    def test_positive_interest_and_invalid(self) -> None:
        rows = build_amortization_schedule(1200.0, 0.12, 12)
        self.assertEqual(len(rows), 12)
        self.assertEqual(rows[-1][3], 0.0)
        with self.assertRaises(ValueError):
            build_amortization_schedule(0.0, 0.05, 12)
