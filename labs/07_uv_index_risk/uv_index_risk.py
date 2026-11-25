"""Lab 07: UV Index Risk."""

import math

_UV_BRACKETS: tuple[tuple[float, str], ...] = (
    (3.0, "low"),
    (6.0, "moderate"),
    (8.0, "high"),
    (11.0, "very high"),
)


def classify_uv_risk(uv_index: float) -> str:
    """Return the WHO UV risk category for a non-negative finite uv_index."""
    if not math.isfinite(uv_index) or uv_index < 0.0:
        raise ValueError(f"uv_index must be finite and non-negative, got {uv_index}")
    for upper_bound, category in _UV_BRACKETS:
        if uv_index < upper_bound:
            return category
    return "extreme"


def needs_sun_protection(uv_index: float) -> bool:
    """Return True if sun protection is advised (UV index >= 3.0)."""
    return classify_uv_risk(uv_index) != "low"


if __name__ == "__main__":
    print("UV 6.5:", classify_uv_risk(6.5), "protect:", needs_sun_protection(6.5))
