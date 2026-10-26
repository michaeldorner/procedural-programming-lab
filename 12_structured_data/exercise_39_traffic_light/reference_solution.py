from enum import Enum


class TrafficLight(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

def can_cross(
    light: TrafficLight,
) -> bool:
    return light == TrafficLight.GREEN
