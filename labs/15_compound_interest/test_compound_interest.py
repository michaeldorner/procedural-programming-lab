"""Unit tests for compound_interest."""

import unittest

from .compound_interest import simulate_yearly_balances, count_years_to_target


class TestCompoundInterest(unittest.TestCase):
    """Tests for simulate_yearly_balances and count_years_to_target."""

    def test_yearly_balances(self) -> None:
        self.assertEqual(simulate_yearly_balances(1000.0, 0.05, 2), [1000.0, 1050.0, 1102.5])
        self.assertEqual(simulate_yearly_balances(1000.0, 0.05, 0), [1000.0])
        with self.assertRaises(ValueError):
            simulate_yearly_balances(-1.0, 0.05, 2)

    def test_years_to_target(self) -> None:
        self.assertEqual(count_years_to_target(1000.0, 0.10, 1000.0), 0)
        self.assertEqual(count_years_to_target(1000.0, 0.10, 1200.0), 2)
        self.assertIsNone(count_years_to_target(1000.0, 0.0, 1200.0))
        with self.assertRaises(ValueError):
            count_years_to_target(0.0, 0.05, 1200.0)
