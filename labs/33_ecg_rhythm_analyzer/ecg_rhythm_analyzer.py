"""Lab 33: ECG Rhythm Analyzer."""

import math


def detect_r_peaks(
    samples: list[float],
    sample_rate_hz: float,
    threshold: float,
) -> list[int]:
    """Return R-peak indices >= threshold with a 200 ms refractory period."""
    if len(samples) < 3 or sample_rate_hz <= 0.0:
        return []
    refractory_samples: int = int(0.2 * sample_rate_hz)
    peaks: list[int] = []
    last_peak: int = -refractory_samples - 1
    for idx in range(1, len(samples) - 1):
        if idx - last_peak < refractory_samples:
            continue
        if samples[idx] >= threshold and samples[idx - 1] < samples[idx] >= samples[idx + 1]:
            peaks.append(idx)
            last_peak = idx
    return peaks


def compute_ecg_metrics(
    peak_indices: list[int],
    sample_rate_hz: float,
) -> tuple[float, float] | None:
    """Return (bpm, rmssd_ms) from peak_indices, or None if fewer than 2 peaks."""
    if len(peak_indices) < 2 or sample_rate_hz <= 0.0:
        return None
    rr_ms: list[float] = [
        (peak_indices[i + 1] - peak_indices[i]) / sample_rate_hz * 1000.0
        for i in range(len(peak_indices) - 1)
    ]
    mean_rr: float = sum(rr_ms) / len(rr_ms)
    bpm: float = 60000.0 / mean_rr
    if len(rr_ms) < 2:
        return (bpm, 0.0)
    sq_diffs: list[float] = [
        (rr_ms[i + 1] - rr_ms[i]) ** 2 for i in range(len(rr_ms) - 1)
    ]
    rmssd: float = math.sqrt(sum(sq_diffs) / len(sq_diffs))
    return (bpm, rmssd)


if __name__ == "__main__":
    print(compute_ecg_metrics([100, 350, 600], 250.0))
