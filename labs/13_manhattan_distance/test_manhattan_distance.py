"""Unit tests for manhattan_distance."""

import unittest

from .manhattan_distance import calculate_manhattan_distance


class TestManhattanDistance(unittest.TestCase):
    """Tests for calculate_manhattan_distance."""

    def test_2d_and_3d_distances(self) -> None:
        self.assertEqual(calculate_manhattan_distance((1, 2), (4, 6)), 7)
        self.assertEqual(calculate_manhattan_distance((-2, 5), (3, -1)), 11)
        self.assertEqual(calculate_manhattan_distance((-1, 0, 2), (2, -3, 2)), 6)
        self.assertEqual(calculate_manhattan_distance((), ()), 0)

    def test_mismatched_dimensions_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            calculate_manhattan_distance((1, 2), (1, 2, 3))
