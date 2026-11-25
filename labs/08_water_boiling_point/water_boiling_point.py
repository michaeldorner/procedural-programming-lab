"""Lab 08: Water Boiling Point."""

import math

MIN_ALTITUDE_M: float = -500.0
MAX_ALTITUDE_M: float = 9000.0


def estimate_boiling_point_c(altitude_m: float) -> float:
    """Return estimated water boiling point in C for altitude_m in [-500, 9000].

    Raises:
        ValueError: If altitude_m is non-finite or outside [-500.0, 9000.0].
    """
    if not math.isfinite(altitude_m) or not (MIN_ALTITUDE_M <= altitude_m <= MAX_ALTITUDE_M):
        raise ValueError(f"altitude_m must be finite and in [-500, 9000], got {altitude_m}")
    return 100.0 - 0.0033 * altitude_m


if __name__ == "__main__":
    print("3000m:", estimate_boiling_point_c(3000.0))
