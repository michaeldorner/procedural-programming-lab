"""Unit tests for atm_dispenser."""

import unittest

from .atm_dispenser import dispense_banknotes


class TestAtmDispenser(unittest.TestCase):
    """Tests for dispense_banknotes."""

    def test_valid_withdrawals(self) -> None:
        self.assertEqual(dispense_banknotes(180, 500), (1, 1, 1, 1))
        self.assertEqual(dispense_banknotes(300, 300), (3, 0, 0, 0))
        self.assertEqual(dispense_banknotes(30, 100), (0, 0, 1, 1))

    def test_insufficient_funds_returns_none(self) -> None:
        self.assertIsNone(dispense_banknotes(200, 100))
        self.assertIsNone(dispense_banknotes(10, 0))

    def test_invalid_arguments_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            dispense_banknotes(0, 500)
        with self.assertRaises(ValueError):
            dispense_banknotes(-20, 500)
        with self.assertRaises(ValueError):
            dispense_banknotes(55, 500)
        with self.assertRaises(ValueError):
            dispense_banknotes(100, -10)
