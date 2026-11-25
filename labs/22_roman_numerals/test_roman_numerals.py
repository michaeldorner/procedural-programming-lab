"""Unit tests for roman_numerals."""

import unittest

from roman_numerals import int_to_roman, roman_to_int


class TestRomanNumerals(unittest.TestCase):
    """Tests for int_to_roman and roman_to_int."""

    def test_conversions(self) -> None:
        self.assertEqual(int_to_roman(1994), "MCMXCIV")
        self.assertEqual(roman_to_int("mcmxciv"), 1994)
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")
        self.assertEqual(roman_to_int("IV"), 4)

    def test_invalid_and_non_canonical(self) -> None:
        self.assertIsNone(int_to_roman(0))
        self.assertIsNone(int_to_roman(4000))
        self.assertIsNone(roman_to_int(""))
        self.assertIsNone(roman_to_int("IIII"))
        self.assertIsNone(roman_to_int("IC"))
