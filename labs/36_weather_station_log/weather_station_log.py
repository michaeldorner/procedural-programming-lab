"""Lab 36: Weather Station Log."""

from pathlib import Path


def summarize_weather_log(
    log_path: Path,
) -> dict[str, tuple[float, float, float]] | None:
    """Return {date: (min_c, max_c, mean_c)} from log_path, or None on OSError."""
    raise NotImplementedError


if __name__ == "__main__":
    print(summarize_weather_log(Path("weather.log")))
