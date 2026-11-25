"""Unit tests for moving_average."""

import unittest

from .moving_average import calculate_moving_average


class TestMovingAverage(unittest.TestCase):
    """Tests for calculate_moving_average."""

    def test_valid_windows(self) -> None:
        data = [1.0, 2.0, 3.0, 4.0]
        self.assertEqual(calculate_moving_average(data, 2), [1.5, 2.5, 3.5])
        self.assertEqual(data, [1.0, 2.0, 3.0, 4.0])
        self.assertEqual(calculate_moving_average([1.0], 3), [])

    def test_invalid_window_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            calculate_moving_average([1.0, 2.0], 0)
        with self.assertRaises(ValueError):
            calculate_moving_average([1.0, 2.0], -2)
