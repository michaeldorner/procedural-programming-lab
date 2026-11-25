"""Lab 03: Temperature Scales."""

import math

ABSOLUTE_ZERO_CELSIUS: float = -273.15
ABSOLUTE_ZERO_FAHRENHEIT: float = -459.67


def _validate_finite_min(value: float, min_value: float, scale: str) -> None:
    """Raise ValueError if value is non-finite or below absolute zero."""
    if not math.isfinite(value) or value < min_value:
        raise ValueError(
            f"{scale} temperature must be finite and >= {min_value}, got {value}"
        )


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit, rejecting temperatures below absolute zero."""
    _validate_finite_min(celsius, ABSOLUTE_ZERO_CELSIUS, "Celsius")
    return celsius * 9.0 / 5.0 + 32.0


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius, rejecting temperatures below absolute zero."""
    _validate_finite_min(fahrenheit, ABSOLUTE_ZERO_FAHRENHEIT, "Fahrenheit")
    return (fahrenheit - 32.0) * 5.0 / 9.0


def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin, rejecting temperatures below absolute zero."""
    _validate_finite_min(celsius, ABSOLUTE_ZERO_CELSIUS, "Celsius")
    return celsius + 273.15


if __name__ == "__main__":
    print("25 C -> F:", celsius_to_fahrenheit(25.0))
    print("77 F -> C:", fahrenheit_to_celsius(77.0))
    print("25 C -> K:", celsius_to_kelvin(25.0))
