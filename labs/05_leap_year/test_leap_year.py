"""Unit tests for leap_year."""

import unittest

from .leap_year import is_leap_year


class TestLeapYear(unittest.TestCase):
    """Tests for is_leap_year."""

    def test_leap_years(self) -> None:
        self.assertIs(is_leap_year(2024), True)
        self.assertIs(is_leap_year(2000), True)

    def test_non_leap_and_non_positive(self) -> None:
        self.assertIs(is_leap_year(1900), False)
        self.assertIs(is_leap_year(2023), False)
        self.assertIs(is_leap_year(0), False)
        self.assertIs(is_leap_year(-4), False)
