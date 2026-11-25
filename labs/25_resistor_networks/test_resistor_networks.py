"""Unit tests for resistor_networks."""

import unittest

from resistor_networks import nearest_e12_value, parallel_resistance, series_resistance


class TestResistorNetworks(unittest.TestCase):
    """Tests for resistor network and E12 helpers."""

    def test_series_and_parallel(self) -> None:
        self.assertAlmostEqual(series_resistance([100.0, 220.0]), 320.0)
        self.assertAlmostEqual(parallel_resistance([100.0, 100.0]), 50.0)
        with self.assertRaises(ValueError):
            series_resistance([])
        with self.assertRaises(ValueError):
            parallel_resistance([100.0, 0.0])

    def test_nearest_e12_value(self) -> None:
        self.assertAlmostEqual(nearest_e12_value(460.0), 470.0)
        self.assertAlmostEqual(nearest_e12_value(9.9), 10.0)
        with self.assertRaises(ValueError):
            nearest_e12_value(0.0)
