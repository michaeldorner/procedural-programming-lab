"""Unit tests for battery_pack_sizing."""

import unittest

from .battery_pack_sizing import calculate_charge_time_hours, calculate_pack_energy_wh, calculate_pack_voltage


class TestBatteryPackSizing(unittest.TestCase):
    """Tests for battery sizing helpers."""

    def test_pack_voltage_and_energy(self) -> None:
        self.assertAlmostEqual(calculate_pack_voltage(3.6, 10), 36.0)
        self.assertAlmostEqual(calculate_pack_energy_wh(3.6, 2.5, 10, 4), 360.0)

    def test_charge_time_hours(self) -> None:
        self.assertAlmostEqual(calculate_charge_time_hours(360.0, 100.0, 0.9), 4.0)

    def test_invalid_inputs_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            calculate_pack_voltage(0.0, 10)
        with self.assertRaises(ValueError):
            calculate_pack_energy_wh(3.6, 2.5, 10, 0)
        with self.assertRaises(ValueError):
            calculate_charge_time_hours(100.0, 50.0, 1.2)
        with self.assertRaises(ValueError):
            calculate_charge_time_hours(100.0, 0.0, 0.9)
