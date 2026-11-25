"""Lab 11: Moon Phase."""

SYNODIC_MONTH_DAYS: float = 29.530588


def lunar_age_days(days_since_reference: int) -> float:
    """Return lunar age in days within [0.0, SYNODIC_MONTH_DAYS)."""
    raise NotImplementedError


def classify_moon_phase(age_days: float) -> str:
    """Classify age_days into one of the 8 standard lunar phase names."""
    raise NotImplementedError


if __name__ == "__main__":
    age = lunar_age_days(15)
    print(f"Day 15 -> age {age:.2f}, phase={classify_moon_phase(age)}")
