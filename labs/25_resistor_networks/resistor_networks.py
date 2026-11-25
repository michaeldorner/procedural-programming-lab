"""Lab 25: Resistor Networks."""

import math

E12_BASE: tuple[float, ...] = (1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2)


def _validate_resistors(resistors: list[float]) -> None:
    if not resistors or any(r <= 0.0 for r in resistors):
        raise ValueError("resistors must be a non-empty list of positive values")


def series_resistance(resistors: list[float]) -> float:
    """Return total series resistance in ohms.

    Raises:
        ValueError: If resistors is empty or contains non-positive values.
    """
    _validate_resistors(resistors)
    return sum(resistors)


def parallel_resistance(resistors: list[float]) -> float:
    """Return total parallel resistance in ohms.

    Raises:
        ValueError: If resistors is empty or contains non-positive values.
    """
    _validate_resistors(resistors)
    return 1.0 / sum(1.0 / r for r in resistors)


def nearest_e12_value(target_ohms: float) -> float:
    """Return nearest standard E12 resistor value for positive target_ohms.

    Raises:
        ValueError: If target_ohms <= 0.0.
    """
    if target_ohms <= 0.0:
        raise ValueError(f"target_ohms must be positive, got {target_ohms}")
    decade: int = math.floor(math.log10(target_ohms))
    candidates: list[float] = [
        round(base * (10.0 ** exp), 6)
        for exp in (decade - 1, decade, decade + 1)
        for base in E12_BASE
    ]
    return min(candidates, key=lambda val: abs(val - target_ohms))


if __name__ == "__main__":
    print("parallel 100||100:", parallel_resistance([100.0, 100.0]))
    print("nearest E12 to 460:", nearest_e12_value(460.0))
