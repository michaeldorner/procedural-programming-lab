"""Lab 08: Water Boiling Point."""

MIN_ALTITUDE_M: float = -500.0
MAX_ALTITUDE_M: float = 9000.0


def estimate_boiling_point_c(altitude_m: float) -> float:
    """Return estimated water boiling point in C for altitude_m in [-500, 9000].

Raises:
    ValueError: If altitude_m is non-finite or outside [-500.0, 9000.0].
    """
    raise NotImplementedError


if __name__ == "__main__":
    print("3000m:", estimate_boiling_point_c(3000.0))
