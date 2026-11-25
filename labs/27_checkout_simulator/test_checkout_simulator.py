"""Unit tests for checkout_simulator."""

import unittest

from checkout_simulator import simulate_checkout


class TestCheckoutSimulator(unittest.TestCase):
    """Tests for simulate_checkout."""

    def test_lane_assignment_and_clearing_time(self) -> None:
        self.assertEqual(simulate_checkout([5, 3, 2, 4], 2), ([9, 5], 9))
        self.assertEqual(simulate_checkout([], 3), ([0, 0, 0], 0))

    def test_invalid_inputs_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            simulate_checkout([5, 3], 0)
        with self.assertRaises(ValueError):
            simulate_checkout([5, -1], 2)
