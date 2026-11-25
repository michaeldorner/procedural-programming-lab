"""Lab 36: Weather Station Log."""

import math
from pathlib import Path


def summarize_weather_log(
    log_path: Path,
) -> dict[str, tuple[float, float, float]] | None:
    """Return {date: (min_c, max_c, mean_c)} from log_path, or None on OSError."""
    readings_by_date: dict[str, list[float]] = {}
    try:
        with open(log_path, encoding="utf-8") as handle:
            for raw_line in handle:
                stripped: str = raw_line.strip()
                if not stripped or stripped.startswith("#") or "," not in stripped:
                    continue
                raw_date, _, raw_temp = stripped.partition(",")
                date_str: str = raw_date.strip()
                if not date_str:
                    continue
                try:
                    temp_c: float = float(raw_temp.strip())
                except ValueError:
                    continue
                if not math.isfinite(temp_c):
                    continue
                readings_by_date.setdefault(date_str, []).append(temp_c)
    except OSError:
        return None

    return {
        date_str: (
            min(vals),
            max(vals),
            round(sum(vals) / len(vals), 2),
        )
        for date_str, vals in readings_by_date.items()
    }


if __name__ == "__main__":
    print(summarize_weather_log(Path("weather.log")))
