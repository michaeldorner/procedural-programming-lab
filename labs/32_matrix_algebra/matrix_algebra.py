"""Lab 32: Matrix Algebra."""


def _shape(matrix: list[list[float]]) -> tuple[int, int]:
    if not matrix or not matrix[0]:
        raise ValueError("Matrix must be non-empty")
    cols: int = len(matrix[0])
    if any(len(row) != cols for row in matrix):
        raise ValueError("Matrix rows must have equal length")
    return (len(matrix), cols)


def add_matrices(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Return element-wise sum a + b.

    Raises:
        ValueError: If matrices are invalid or have mismatched shapes.
    """
    sa = _shape(a)
    sb = _shape(b)
    if sa != sb:
        raise ValueError(f"Matrix shapes must match, got {sa} and {sb}")
    rows, cols = sa
    return [[a[r][c] + b[r][c] for c in range(cols)] for r in range(rows)]


def scale_matrix(matrix: list[list[float]], factor: float) -> list[list[float]]:
    """Return matrix scaled by factor."""
    _shape(matrix)
    return [[val * factor for val in row] for row in matrix]


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """Return transpose of matrix."""
    rows, cols = _shape(matrix)
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def multiply_matrices(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Return matrix product a @ b.

    Raises:
        ValueError: If matrices are invalid or inner dimensions do not match.
    """
    sa = _shape(a)
    sb = _shape(b)
    if sa[1] != sb[0]:
        raise ValueError(f"Incompatible shapes for multiplication: {sa} and {sb}")
    rows_a, shared = sa
    cols_b = sb[1]
    return [
        [sum(a[r][k] * b[k][c] for k in range(shared)) for c in range(cols_b)]
        for r in range(rows_a)
    ]


if __name__ == "__main__":
    print(multiply_matrices([[1.0, 2.0], [3.0, 4.0]], [[2.0, 0.0], [1.0, 2.0]]))
