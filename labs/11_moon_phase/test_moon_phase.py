"""Unit tests for moon_phase."""

import math
import unittest

from moon_phase import classify_moon_phase, lunar_age_days


class TestMoonPhase(unittest.TestCase):
    """Tests for lunar age and 8-phase classification."""

    def test_lunar_age_days(self) -> None:
        self.assertAlmostEqual(lunar_age_days(0), 0.0)
        self.assertAlmostEqual(lunar_age_days(30), 0.469412, places=4)

    def test_classify_moon_phase(self) -> None:
        self.assertEqual(classify_moon_phase(0.0), "new moon")
        self.assertEqual(classify_moon_phase(5.0), "waxing crescent")
        self.assertEqual(classify_moon_phase(8.0), "first quarter")
        self.assertEqual(classify_moon_phase(12.0), "waxing gibbous")
        self.assertEqual(classify_moon_phase(15.0), "full moon")
        self.assertEqual(classify_moon_phase(20.0), "waning gibbous")
        self.assertEqual(classify_moon_phase(23.0), "last quarter")
        self.assertEqual(classify_moon_phase(27.0), "waning crescent")
        with self.assertRaises(ValueError):
            classify_moon_phase(math.nan)
