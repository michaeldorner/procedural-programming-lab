"""Unit tests for weather_station_log."""

from pathlib import Path
import tempfile
import unittest

from weather_station_log import summarize_weather_log


class TestWeatherStationLog(unittest.TestCase):
    """Tests for summarize_weather_log."""

    def test_valid_and_corrupt_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            log_file = Path(tmp_dir) / "weather.log"
            log_file.write_text(
                "# header\n2026-10-01,10.0\nbad_line\n2026-10-01,nan\n2026-10-01,20.0\n2026-10-02,15.5\n",
                encoding="utf-8",
            )
            self.assertEqual(
                summarize_weather_log(log_file),
                {"2026-10-01": (10.0, 20.0, 15.0), "2026-10-02": (15.5, 15.5, 15.5)},
            )

    def test_missing_file_returns_none(self) -> None:
        self.assertIsNone(summarize_weather_log(Path("missing_weather.log")))
