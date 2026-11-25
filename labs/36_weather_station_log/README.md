# Lab 36: Weather Station Log

**Topics:** File I/O, exception handling, string parsing, dictionaries  
**Lectures:** 07 (Validation & Exceptions), 09 (Built-in Collections), 15 (File Processing)

Read a weather station log file, ignore corrupt lines, and compute daily minimum, maximum, and mean temperatures.

## Requirements

- Implement `summarize_weather_log` to return no value if the file cannot be opened or read.
- Ignore blank lines, `#` comments, and malformed entries (missing comma, blank date, or non-finite/non-numeric temperature).
- Return daily `(min, max, mean)` tuples with the mean rounded to 2 decimal places.

## Worked Examples

- Readings 10.0 and 20.0 on 2026-10-01 summarize to (10.0, 20.0, 15.0).

## Implementation Hints

- See [`open()`](https://docs.python.org/3/library/functions.html#open), [`math.isfinite()`](https://docs.python.org/3/library/math.html#math.isfinite), and [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError).

## Run & Test

```bash
python weather_station_log.py
python -m unittest
```
