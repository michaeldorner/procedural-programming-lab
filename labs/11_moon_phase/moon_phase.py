"""Lab 11: Moon Phase."""

import math

SYNODIC_MONTH_DAYS: float = 29.530588


def lunar_age_days(days_since_reference: int) -> float:
    """Return lunar age in days within [0.0, SYNODIC_MONTH_DAYS)."""
    return days_since_reference % SYNODIC_MONTH_DAYS


def classify_moon_phase(age_days: float) -> str:
    """Classify age_days into one of the 8 standard lunar phase names."""
    if not math.isfinite(age_days):
        raise ValueError(f"age_days must be finite, got {age_days}")
    normalized: float = age_days % SYNODIC_MONTH_DAYS
    octant: float = SYNODIC_MONTH_DAYS / 8.0
    if normalized < octant:
        return "new moon"
    if normalized < 2.0 * octant:
        return "waxing crescent"
    if normalized < 3.0 * octant:
        return "first quarter"
    if normalized < 4.0 * octant:
        return "waxing gibbous"
    if normalized < 5.0 * octant:
        return "full moon"
    if normalized < 6.0 * octant:
        return "waning gibbous"
    if normalized < 7.0 * octant:
        return "last quarter"
    return "waning crescent"


if __name__ == "__main__":
    age = lunar_age_days(15)
    print(f"Day 15 -> age {age:.2f}, phase={classify_moon_phase(age)}")
