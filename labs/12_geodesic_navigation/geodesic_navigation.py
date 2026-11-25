"""Lab 12: Geodesic Navigation."""

EARTH_RADIUS_KM: float = 6371.0
MIN_LATITUDE: float = -90.0
MAX_LATITUDE: float = 90.0
MIN_LONGITUDE: float = -180.0
MAX_LONGITUDE: float = 180.0
Coords = tuple[float, float]


def haversine_distance_km(origin: Coords, destination: Coords) -> float:
    """Return great-circle distance in km between two `(lat, lon)` degree pairs.

Raises:
    ValueError: If either coordinate has latitude outside [-90, 90]
        or longitude outside [-180, 180].
    """
    raise NotImplementedError


if __name__ == "__main__":
    chemnitz: Coords = (50.8278, 12.9214)
    berlin: Coords = (52.5200, 13.4050)
    print("Chemnitz -> Berlin km:",
          round(haversine_distance_km(chemnitz, berlin), 2))
