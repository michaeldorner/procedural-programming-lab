"""Unit tests for interval_scheduler."""

import unittest

from interval_scheduler import select_max_meetings


class TestIntervalScheduler(unittest.TestCase):
    """Tests for select_max_meetings."""

    def test_greedy_selection(self) -> None:
        meetings = [(1, 4), (3, 5), (0, 6), (4, 7)]
        self.assertEqual(select_max_meetings(meetings), [(1, 4), (4, 7)])
        self.assertEqual(select_max_meetings([]), [])

    def test_invalid_interval_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            select_max_meetings([(5, 5)])
        with self.assertRaises(ValueError):
            select_max_meetings([(6, 4)])
