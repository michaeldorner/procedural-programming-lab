"""Unit tests for solar_time."""

import unittest

from solar_time import apparent_solar_hour, solar_noon_offset_minutes


class TestSolarTime(unittest.TestCase):
    """Tests for solar time calculations."""

    def test_solar_noon_offset_minutes(self) -> None:
        self.assertAlmostEqual(solar_noon_offset_minutes(12.92, 15.0, 0.0), 8.32)
        self.assertAlmostEqual(solar_noon_offset_minutes(15.0, 15.0, 5.0), -5.0)

    def test_apparent_solar_hour_wrap_around(self) -> None:
        self.assertAlmostEqual(apparent_solar_hour(0.1, 0.0, 15.0, 0.0), 23.1)
        self.assertAlmostEqual(apparent_solar_hour(23.5, 30.0, 15.0, 0.0), 0.5)

    def test_invalid_coordinates_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            solar_noon_offset_minutes(181.0, 15.0, 0.0)
        with self.assertRaises(ValueError):
            apparent_solar_hour(12.0, 15.0, -181.0, 0.0)
