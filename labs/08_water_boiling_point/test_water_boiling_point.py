"""Unit tests for water_boiling_point."""

import math
import unittest

from water_boiling_point import estimate_boiling_point_c


class TestWaterBoilingPoint(unittest.TestCase):
    """Tests for estimate_boiling_point_c."""

    def test_valid_altitudes(self) -> None:
        self.assertAlmostEqual(estimate_boiling_point_c(0.0), 100.0)
        self.assertAlmostEqual(estimate_boiling_point_c(3000.0), 90.1)
        self.assertAlmostEqual(estimate_boiling_point_c(-500.0), 101.65)
        self.assertAlmostEqual(estimate_boiling_point_c(9000.0), 70.3)

    def test_out_of_range_raises_value_error(self) -> None:
        for bad in (-500.1, 9000.1, math.nan, math.inf):
            with self.assertRaises(ValueError):
                estimate_boiling_point_c(bad)
