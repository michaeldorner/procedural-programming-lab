"""Lab 33: ECG Rhythm Analyzer."""


def detect_r_peaks(
    samples: list[float],
    sample_rate_hz: float,
    threshold: float,
) -> list[int]:
    """Return R-peak indices >= threshold with a 200 ms refractory period."""
    raise NotImplementedError


def compute_ecg_metrics(
    peak_indices: list[int],
    sample_rate_hz: float,
) -> tuple[float, float] | None:
    """Return (bpm, rmssd_ms) from peak_indices, or None if fewer than 2 peaks."""
    raise NotImplementedError


if __name__ == "__main__":
    print(compute_ecg_metrics([100, 350, 600], 250.0))
