import math


# Student template

def celsius_to_fahrenheit(
    celsius: float,
) -> float:
    pass


def fahrenheit_to_celsius(
    fahrenheit: float,
) -> float:
    pass


# Basic solution

def celsius_to_fahrenheit(
    celsius: float,
) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(
    fahrenheit: float,
) -> float:
    return (fahrenheit - 32) * 5 / 9


# Excellent solution for bonus tests

def _validate_celsius(
    celsius: float,
) -> None:
    if not math.isfinite(
        celsius,
    ):
        raise ValueError(
            "Temperature must be a finite number."
        )

    if celsius < -273.15:
        raise ValueError(
            "Temperature below absolute zero."
        )


def _validate_fahrenheit(
    fahrenheit: float,
) -> None:
    if not math.isfinite(
        fahrenheit,
    ):
        raise ValueError(
            "Temperature must be a finite number."
        )

    if fahrenheit < -459.67:
        raise ValueError(
            "Temperature below absolute zero."
        )


def celsius_to_fahrenheit(
    celsius: float,
) -> float:
    _validate_celsius(
        celsius,
    )

    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(
    fahrenheit: float,
) -> float:
    _validate_fahrenheit(
        fahrenheit,
    )

    return (fahrenheit - 32) * 5 / 9


``
