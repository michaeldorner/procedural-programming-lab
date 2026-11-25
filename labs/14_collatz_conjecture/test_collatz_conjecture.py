"""Unit tests for collatz_conjecture."""

import unittest

from collatz_conjecture import collatz_peak, collatz_sequence, collatz_stopping_time


class TestCollatzConjecture(unittest.TestCase):
    """Tests for Collatz sequence, stopping time, and peak."""

    def test_valid_sequences(self) -> None:
        self.assertEqual(collatz_sequence(1), [1])
        self.assertEqual(collatz_sequence(6), [6, 3, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(collatz_stopping_time(1), 0)
        self.assertEqual(collatz_stopping_time(6), 8)
        self.assertEqual(collatz_peak(6), 16)

    def test_non_positive_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            collatz_sequence(0)
        with self.assertRaises(ValueError):
            collatz_stopping_time(-3)
        with self.assertRaises(ValueError):
            collatz_peak(0)
