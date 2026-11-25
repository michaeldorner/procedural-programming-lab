"""Unit tests for collatz_conjecture."""

import unittest

from .collatz_conjecture import find_collatz_peak, generate_collatz_sequence, count_collatz_steps


class TestCollatzConjecture(unittest.TestCase):
    """Tests for Collatz sequence, stopping time, and peak."""

    def test_valid_sequences(self) -> None:
        self.assertEqual(generate_collatz_sequence(1), [1])
        self.assertEqual(generate_collatz_sequence(6), [6, 3, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(count_collatz_steps(1), 0)
        self.assertEqual(count_collatz_steps(6), 8)
        self.assertEqual(find_collatz_peak(6), 16)

    def test_non_positive_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            generate_collatz_sequence(0)
        with self.assertRaises(ValueError):
            count_collatz_steps(-3)
        with self.assertRaises(ValueError):
            find_collatz_peak(0)
