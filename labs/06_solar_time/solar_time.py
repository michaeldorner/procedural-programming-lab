"""Lab 06: Solar Time."""


def solar_noon_offset_minutes(
    longitude_deg: float,
    meridian_deg: float,
    equation_of_time_min: float,
) -> float:
    """Return solar noon offset in minutes from standard clock noon."""
    raise NotImplementedError


def apparent_solar_hour(
    standard_hour: float,
    longitude_deg: float,
    meridian_deg: float,
    equation_of_time_min: float,
) -> float:
    """Return apparent solar hour wrapped into [0.0, 24.0)."""
    raise NotImplementedError


if __name__ == "__main__":
    print("Chemnitz offset min:", solar_noon_offset_minutes(12.92, 15.0, 0.0))
