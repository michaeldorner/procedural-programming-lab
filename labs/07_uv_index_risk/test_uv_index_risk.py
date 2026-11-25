"""Unit tests for uv_index_risk."""

import math
import unittest

from .uv_index_risk import classify_uv_risk, needs_sun_protection


class TestUvIndexRisk(unittest.TestCase):
    """Tests for UV risk classification."""

    def test_brackets_and_boundaries(self) -> None:
        self.assertEqual(classify_uv_risk(0.0), "low")
        self.assertEqual(classify_uv_risk(2.9), "low")
        self.assertEqual(classify_uv_risk(3.0), "moderate")
        self.assertEqual(classify_uv_risk(6.0), "high")
        self.assertEqual(classify_uv_risk(8.0), "very high")
        self.assertEqual(classify_uv_risk(11.0), "extreme")

    def test_invalid_uv_index_raises_value_error(self) -> None:
        for bad_value in (-0.1, math.nan, math.inf):
            with self.assertRaises(ValueError):
                classify_uv_risk(bad_value)

    def test_needs_sun_protection(self) -> None:
        self.assertIs(needs_sun_protection(2.9), False)
        self.assertIs(needs_sun_protection(3.0), True)
        with self.assertRaises(ValueError):
            needs_sun_protection(-1.0)
