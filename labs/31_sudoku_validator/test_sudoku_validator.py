"""Unit tests for sudoku_validator."""

import unittest

from sudoku_validator import is_valid_sudoku


class TestSudokuValidator(unittest.TestCase):
    """Tests for is_valid_sudoku."""

    def test_valid_and_invalid_boards(self) -> None:
        valid = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
        self.assertIs(is_valid_sudoku(valid), True)
        bad_box = [row[:] for row in valid]
        bad_box[0][0], bad_box[0][1] = bad_box[0][1], bad_box[0][0]
        self.assertIs(is_valid_sudoku(bad_box), False)
        self.assertIs(is_valid_sudoku([[1, 2, 3]]), False)
