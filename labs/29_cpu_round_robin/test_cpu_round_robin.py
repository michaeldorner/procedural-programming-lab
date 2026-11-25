"""Unit tests for cpu_round_robin."""

import unittest

from cpu_round_robin import round_robin_completion_times


class TestCpuRoundRobin(unittest.TestCase):
    """Tests for round_robin_completion_times."""

    def test_round_robin_schedule(self) -> None:
        self.assertEqual(round_robin_completion_times([5, 3, 1], 2), [9, 8, 5])
        self.assertEqual(round_robin_completion_times([], 2), [])

    def test_invalid_inputs_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            round_robin_completion_times([5, 3], 0)
        with self.assertRaises(ValueError):
            round_robin_completion_times([5, 0], 2)
