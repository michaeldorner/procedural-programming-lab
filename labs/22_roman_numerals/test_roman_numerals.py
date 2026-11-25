"""Unit tests for roman_numerals."""

import unittest

from .roman_numerals import convert_int_to_roman, convert_roman_to_int


class TestRomanNumerals(unittest.TestCase):
    """Tests for convert_int_to_roman and convert_roman_to_int."""

    def test_conversions(self) -> None:
        self.assertEqual(convert_int_to_roman(1994), "MCMXCIV")
        self.assertEqual(convert_roman_to_int("mcmxciv"), 1994)
        self.assertEqual(convert_int_to_roman(3999), "MMMCMXCIX")
        self.assertEqual(convert_roman_to_int("IV"), 4)

    def test_invalid_and_non_canonical(self) -> None:
        self.assertIsNone(convert_int_to_roman(0))
        self.assertIsNone(convert_int_to_roman(4000))
        self.assertIsNone(convert_roman_to_int(""))
        self.assertIsNone(convert_roman_to_int("IIII"))
        self.assertIsNone(convert_roman_to_int("IC"))
