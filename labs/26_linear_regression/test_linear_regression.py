"""Unit tests for linear_regression."""

import unittest

from .linear_regression import fit_linear_regression


class TestLinearRegression(unittest.TestCase):
    """Tests for fit_linear_regression."""

    def test_exact_line_and_constant_y(self) -> None:
        m, b, r2 = fit_linear_regression([1.0, 2.0, 3.0], [3.0, 5.0, 7.0])
        self.assertAlmostEqual(m, 2.0)
        self.assertAlmostEqual(b, 1.0)
        self.assertAlmostEqual(r2, 1.0)
        self.assertEqual(fit_linear_regression([1.0, 2.0], [5.0, 5.0]), (0.0, 5.0, 1.0))

    def test_invalid_inputs_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            fit_linear_regression([1.0], [2.0])
        with self.assertRaises(ValueError):
            fit_linear_regression([1.0, 2.0], [1.0])
        with self.assertRaises(ValueError):
            fit_linear_regression([2.0, 2.0], [1.0, 3.0])
