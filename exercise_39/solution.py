from enum import Enum


class TrafficLight(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"


# Student template
def can_cross(
    light: TrafficLight,
) -> bool:
    pass


# Basic solution
def can_cross(
    light: TrafficLight,
) -> bool:
    return light == TrafficLight.GREEN


# Excellent solution for bonus tests
def can_cross(
    light: TrafficLight,
) -> bool:
    return light == TrafficLight.GREEN
