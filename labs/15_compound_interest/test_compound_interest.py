"""Unit tests for compound_interest."""

import unittest

from compound_interest import yearly_balances, years_to_target


class TestCompoundInterest(unittest.TestCase):
    """Tests for yearly_balances and years_to_target."""

    def test_yearly_balances(self) -> None:
        self.assertEqual(yearly_balances(1000.0, 0.05, 2), [1000.0, 1050.0, 1102.5])
        self.assertEqual(yearly_balances(1000.0, 0.05, 0), [1000.0])
        with self.assertRaises(ValueError):
            yearly_balances(-1.0, 0.05, 2)

    def test_years_to_target(self) -> None:
        self.assertEqual(years_to_target(1000.0, 0.10, 1000.0), 0)
        self.assertEqual(years_to_target(1000.0, 0.10, 1200.0), 2)
        self.assertIsNone(years_to_target(1000.0, 0.0, 1200.0))
        with self.assertRaises(ValueError):
            years_to_target(0.0, 0.05, 1200.0)
