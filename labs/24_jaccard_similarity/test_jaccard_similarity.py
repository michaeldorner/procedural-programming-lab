"""Unit tests for calculate_jaccard_similarity."""

import unittest

from .jaccard_similarity import (
    calculate_jaccard_similarity,
    calculate_overlap_coefficient,
    find_symmetric_difference,
)


class TestJaccardSimilarity(unittest.TestCase):
    """Tests for set similarity metrics."""

    def test_metrics_and_empty_sets(self) -> None:
        self.assertAlmostEqual(calculate_jaccard_similarity({"a", "b"}, {"b", "c"}), 1.0 / 3.0)
        self.assertAlmostEqual(calculate_jaccard_similarity(set(), set()), 1.0)
        self.assertAlmostEqual(calculate_overlap_coefficient({"a"}, {"a", "b"}), 1.0)
        self.assertAlmostEqual(calculate_overlap_coefficient(set(), {"a"}), 0.0)
        self.assertEqual(find_symmetric_difference({"a", "b"}, {"b", "c"}), {"a", "c"})
