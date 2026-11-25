"""Unit tests for cpu_round_robin."""

import unittest

from .cpu_round_robin import simulate_round_robin


class TestCpuRoundRobin(unittest.TestCase):
    """Tests for simulate_round_robin."""

    def test_round_robin_schedule(self) -> None:
        self.assertEqual(simulate_round_robin([5, 3, 1], 2), [9, 8, 5])
        self.assertEqual(simulate_round_robin([], 2), [])

    def test_invalid_inputs_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            simulate_round_robin([5, 3], 0)
        with self.assertRaises(ValueError):
            simulate_round_robin([5, 0], 2)
