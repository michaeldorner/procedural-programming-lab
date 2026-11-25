"""Lab 25: Resistor Networks."""

E12_BASE: tuple[float, ...] = (1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2)


def calculate_series_resistance(resistors: list[float]) -> float:
    """Return total series resistance in ohms.

Raises:
    ValueError: If resistors is empty or contains non-positive values.
    """
    raise NotImplementedError


def calculate_parallel_resistance(resistors: list[float]) -> float:
    """Return total parallel resistance in ohms.

Raises:
    ValueError: If resistors is empty or contains non-positive values.
    """
    raise NotImplementedError


def find_nearest_e12_value(target_ohms: float) -> float:
    """Return nearest standard E12 resistor value for positive target_ohms.

Raises:
    ValueError: If target_ohms <= 0.0.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print("parallel 100||100:", calculate_parallel_resistance([100.0, 100.0]))
    print("nearest E12 to 460:", find_nearest_e12_value(460.0))
