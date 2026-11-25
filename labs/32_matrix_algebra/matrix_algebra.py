"""Lab 32: Matrix Algebra."""


def add_matrices(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Return element-wise sum a + b.

Raises:
    ValueError: If matrices are invalid or have mismatched shapes.
    """
    raise NotImplementedError


def scale_matrix(matrix: list[list[float]], factor: float) -> list[list[float]]:
    """Return matrix scaled by factor."""
    raise NotImplementedError


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """Return transpose of matrix."""
    raise NotImplementedError


def multiply_matrices(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Return matrix product a @ b.

Raises:
    ValueError: If matrices are invalid or inner dimensions do not match.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(multiply_matrices([[1.0, 2.0], [3.0, 4.0]], [[2.0, 0.0], [1.0, 2.0]]))
