"""Unit tests for battery_pack_sizing."""

import unittest

from battery_pack_sizing import charge_time_hours, pack_energy_wh, pack_voltage


class TestBatteryPackSizing(unittest.TestCase):
    """Tests for battery sizing helpers."""

    def test_pack_voltage_and_energy(self) -> None:
        self.assertAlmostEqual(pack_voltage(3.6, 10), 36.0)
        self.assertAlmostEqual(pack_energy_wh(3.6, 2.5, 10, 4), 360.0)

    def test_charge_time_hours(self) -> None:
        self.assertAlmostEqual(charge_time_hours(360.0, 100.0, 0.9), 4.0)

    def test_invalid_inputs_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            pack_voltage(0.0, 10)
        with self.assertRaises(ValueError):
            pack_energy_wh(3.6, 2.5, 10, 0)
        with self.assertRaises(ValueError):
            charge_time_hours(100.0, 50.0, 1.2)
        with self.assertRaises(ValueError):
            charge_time_hours(100.0, 0.0, 0.9)
