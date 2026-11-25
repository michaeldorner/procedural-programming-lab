"""Unit tests for triangle_geometry."""

import unittest

from triangle_geometry import classify_triangle, is_valid_triangle, triangle_area


class TestTriangleGeometry(unittest.TestCase):
    """Tests for triangle geometry functions."""

    def test_validity(self) -> None:
        self.assertIs(is_valid_triangle(3.0, 4.0, 5.0), True)
        self.assertIs(is_valid_triangle(1.0, 2.0, 3.0), False)
        self.assertIs(is_valid_triangle(0.0, 4.0, 5.0), False)

    def test_classification_and_area(self) -> None:
        self.assertEqual(classify_triangle(3.0, 3.0, 3.0), "equilateral")
        self.assertEqual(classify_triangle(3.0, 3.0, 4.0), "isosceles")
        self.assertEqual(classify_triangle(3.0, 4.0, 5.0), "scalene")
        self.assertAlmostEqual(triangle_area(3.0, 4.0, 5.0), 6.0)
        with self.assertRaises(ValueError):
            classify_triangle(1.0, 2.0, 10.0)
        with self.assertRaises(ValueError):
            triangle_area(1.0, 2.0, 10.0)
