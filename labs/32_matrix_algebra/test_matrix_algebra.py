"""Unit tests for matrix_algebra."""

import unittest

from matrix_algebra import add_matrices, multiply_matrices, scale_matrix, transpose_matrix


class TestMatrixAlgebra(unittest.TestCase):
    """Tests for matrix operations."""

    def test_operations(self) -> None:
        a = [[1.0, 2.0], [3.0, 4.0]]
        b = [[2.0, 0.0], [1.0, 2.0]]
        self.assertEqual(add_matrices(a, b), [[3.0, 2.0], [4.0, 6.0]])
        self.assertEqual(scale_matrix(a, 2.0), [[2.0, 4.0], [6.0, 8.0]])
        self.assertEqual(transpose_matrix([[1.0, 2.0, 3.0]]), [[1.0], [2.0], [3.0]])
        self.assertEqual(multiply_matrices(a, b), [[4.0, 4.0], [10.0, 8.0]])

    def test_invalid_shapes_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            add_matrices([[1.0]], [[1.0, 2.0]])
        with self.assertRaises(ValueError):
            multiply_matrices([[1.0, 2.0]], [[1.0, 2.0]])
        with self.assertRaises(ValueError):
            transpose_matrix([[1.0, 2.0], [3.0]])
