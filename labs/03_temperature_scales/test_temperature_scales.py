"""Unit tests for temperature_scales."""

import math
import unittest

from temperature_scales import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
)


class TestTemperatureScales(unittest.TestCase):
    """Tests for temperature conversion functions."""

    def test_celsius_to_fahrenheit(self) -> None:
        self.assertAlmostEqual(celsius_to_fahrenheit(0.0), 32.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(100.0), 212.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40.0), -40.0)

    def test_fahrenheit_to_celsius(self) -> None:
        self.assertAlmostEqual(fahrenheit_to_celsius(32.0), 0.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212.0), 100.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(-459.67), -273.15, places=2)

    def test_celsius_to_kelvin(self) -> None:
        self.assertAlmostEqual(celsius_to_kelvin(0.0), 273.15)
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0.0)

    def test_below_absolute_zero_and_non_finite_raise_value_error(self) -> None:
        for bad_c in (-273.16, math.nan, math.inf, -math.inf):
            with self.assertRaises(ValueError):
                celsius_to_fahrenheit(bad_c)
            with self.assertRaises(ValueError):
                celsius_to_kelvin(bad_c)
        for bad_f in (-459.68, math.nan, math.inf, -math.inf):
            with self.assertRaises(ValueError):
                fahrenheit_to_celsius(bad_f)
