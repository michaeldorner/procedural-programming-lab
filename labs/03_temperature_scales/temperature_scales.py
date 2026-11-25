"""Lab 03: Temperature Scales."""

ABSOLUTE_ZERO_CELSIUS: float = -273.15
ABSOLUTE_ZERO_FAHRENHEIT: float = -459.67


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit, rejecting temperatures below absolute zero."""
    raise NotImplementedError


def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius, rejecting temperatures below absolute zero."""
    raise NotImplementedError


def convert_celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin, rejecting temperatures below absolute zero."""
    raise NotImplementedError


if __name__ == "__main__":
    print("25 C -> F:", convert_celsius_to_fahrenheit(25.0))
    print("77 F -> C:", convert_fahrenheit_to_celsius(77.0))
    print("25 C -> K:", convert_celsius_to_kelvin(25.0))
