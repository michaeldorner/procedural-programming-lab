"""Unit tests for geodesic_navigation."""

import unittest

from .geodesic_navigation import calculate_haversine_distance_km


class TestGeodesicNavigation(unittest.TestCase):
    """Tests for Haversine distance and coordinate validation."""

    def test_haversine_distance(self) -> None:
        self.assertAlmostEqual(calculate_haversine_distance_km((50.0, 10.0), (50.0, 10.0)), 0.0)
        dist = calculate_haversine_distance_km((50.8278, 12.9214), (52.5200, 13.4050))
        self.assertAlmostEqual(dist, 191.09, places=2)

    def test_invalid_coordinates_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            calculate_haversine_distance_km((95.0, 10.0), (50.0, 10.0))
        with self.assertRaises(ValueError):
            calculate_haversine_distance_km((50.0, 10.0), (50.0, -185.0))
