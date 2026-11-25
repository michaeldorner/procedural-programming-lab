"""Unit tests for resistor_networks."""

import unittest

from .resistor_networks import find_nearest_e12_value, calculate_parallel_resistance, calculate_series_resistance


class TestResistorNetworks(unittest.TestCase):
    """Tests for resistor network and E12 helpers."""

    def test_series_and_parallel(self) -> None:
        self.assertAlmostEqual(calculate_series_resistance([100.0, 220.0]), 320.0)
        self.assertAlmostEqual(calculate_parallel_resistance([100.0, 100.0]), 50.0)
        with self.assertRaises(ValueError):
            calculate_series_resistance([])
        with self.assertRaises(ValueError):
            calculate_parallel_resistance([100.0, 0.0])

    def test_nearest_e12_value(self) -> None:
        self.assertAlmostEqual(find_nearest_e12_value(460.0), 470.0)
        self.assertAlmostEqual(find_nearest_e12_value(9.9), 10.0)
        with self.assertRaises(ValueError):
            find_nearest_e12_value(0.0)
