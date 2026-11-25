"""Unit tests for jaccard_similarity."""

import unittest

from jaccard_similarity import (
    jaccard_similarity,
    overlap_coefficient,
    symmetric_difference,
)


class TestJaccardSimilarity(unittest.TestCase):
    """Tests for set similarity metrics."""

    def test_metrics_and_empty_sets(self) -> None:
        self.assertAlmostEqual(jaccard_similarity({"a", "b"}, {"b", "c"}), 1.0 / 3.0)
        self.assertAlmostEqual(jaccard_similarity(set(), set()), 1.0)
        self.assertAlmostEqual(overlap_coefficient({"a"}, {"a", "b"}), 1.0)
        self.assertAlmostEqual(overlap_coefficient(set(), {"a"}), 0.0)
        self.assertEqual(symmetric_difference({"a", "b"}, {"b", "c"}), {"a", "c"})
