"""Lab 31: Sudoku Validator."""

_EXPECTED_DIGITS: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def is_valid_sudoku(board: list[list[int]]) -> bool:
    """Return True if board is a valid completed 9x9 Sudoku grid."""
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False
    for row in board:
        if set(row) != _EXPECTED_DIGITS:
            return False
    for col in range(9):
        if {board[r][col] for r in range(9)} != _EXPECTED_DIGITS:
            return False
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = {
                board[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            }
            if box != _EXPECTED_DIGITS:
                return False
    return True


if __name__ == "__main__":
    sample = [
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
    print("Valid:", is_valid_sudoku(sample))
