"""Lab 12: Geodesic Navigation."""

import math

EARTH_RADIUS_KM: float = 6371.0
MIN_LATITUDE: float = -90.0
MAX_LATITUDE: float = 90.0
MIN_LONGITUDE: float = -180.0
MAX_LONGITUDE: float = 180.0

Coords = tuple[float, float]


def _validate_coords(point: Coords) -> None:
    """Raise ValueError if latitude or longitude is outside valid WGS84 bounds."""
    lat, lon = point
    if not (MIN_LATITUDE <= lat <= MAX_LATITUDE):
        raise ValueError(f"Latitude must be in [-90.0, 90.0], got {lat}")
    if not (MIN_LONGITUDE <= lon <= MAX_LONGITUDE):
        raise ValueError(f"Longitude must be in [-180.0, 180.0], got {lon}")


def haversine_distance_km(origin: Coords, destination: Coords) -> float:
    """Return great-circle distance in km between two `(lat, lon)` degree pairs.

    Raises:
        ValueError: If either coordinate has latitude outside [-90, 90]
            or longitude outside [-180, 180].
    """
    _validate_coords(origin)
    _validate_coords(destination)

    lat1, lon1 = origin
    lat2, lon2 = destination

    phi1: float = math.radians(lat1)
    phi2: float = math.radians(lat2)
    d_phi: float = math.radians(lat2 - lat1)
    d_lambda: float = math.radians(lon2 - lon1)

    a: float = math.sin(d_phi / 2.0) ** 2 + math.cos(phi1) * \
        math.cos(phi2) * math.sin(d_lambda / 2.0) ** 2
    clamped_a: float = min(1.0, max(0.0, a))
    central_angle: float = 2.0 * \
        math.atan2(math.sqrt(clamped_a), math.sqrt(1.0 - clamped_a))
    return EARTH_RADIUS_KM * central_angle


if __name__ == "__main__":
    chemnitz: Coords = (50.8278, 12.9214)
    berlin: Coords = (52.5200, 13.4050)
    print("Chemnitz -> Berlin km:",
          round(haversine_distance_km(chemnitz, berlin), 2))
