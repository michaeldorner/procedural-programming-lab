"""Lab 06: Solar Time."""

import math


def _validate_degrees(value: float, label: str) -> None:
    """Raise ValueError if value is non-finite or outside [-180.0, 180.0]."""
    if not math.isfinite(value) or not (-180.0 <= value <= 180.0):
        raise ValueError(f"{label} must be finite and in [-180.0, 180.0], got {value}")


def solar_noon_offset_minutes(
    longitude_deg: float,
    meridian_deg: float,
    equation_of_time_min: float,
) -> float:
    """Return solar noon offset in minutes from standard clock noon."""
    _validate_degrees(longitude_deg, "longitude_deg")
    _validate_degrees(meridian_deg, "meridian_deg")
    if not math.isfinite(equation_of_time_min):
        raise ValueError("equation_of_time_min must be finite")
    return 4.0 * (meridian_deg - longitude_deg) - equation_of_time_min


def apparent_solar_hour(
    standard_hour: float,
    longitude_deg: float,
    meridian_deg: float,
    equation_of_time_min: float,
) -> float:
    """Return apparent solar hour wrapped into [0.0, 24.0)."""
    if not math.isfinite(standard_hour):
        raise ValueError("standard_hour must be finite")
    offset_minutes: float = solar_noon_offset_minutes(
        longitude_deg,
        meridian_deg,
        equation_of_time_min,
    )
    return (standard_hour - offset_minutes / 60.0) % 24.0


if __name__ == "__main__":
    print("Chemnitz offset min:", solar_noon_offset_minutes(12.92, 15.0, 0.0))
