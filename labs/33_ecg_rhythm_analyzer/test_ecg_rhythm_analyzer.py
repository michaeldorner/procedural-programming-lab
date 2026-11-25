"""Unit tests for ecg_rhythm_analyzer."""

import unittest

from .ecg_rhythm_analyzer import compute_ecg_metrics, detect_r_peaks


class TestEcgRhythmAnalyzer(unittest.TestCase):
    """Tests for R-peak detection and HRV metrics."""

    def test_detect_r_peaks_with_refractory_window(self) -> None:
        # At 100 Hz, 200 ms = 20 samples
        signal = [0.0] * 60
        signal[10] = 1.2
        signal[15] = 1.1  # within 200 ms refractory window -> ignored
        signal[35] = 1.3
        self.assertEqual(detect_r_peaks(signal, 100.0, 1.0), [10, 35])

    def test_compute_ecg_metrics(self) -> None:
        self.assertIsNone(compute_ecg_metrics([100], 250.0))
        metrics = compute_ecg_metrics([100, 350, 600], 250.0)
        self.assertEqual(metrics, (60.0, 0.0))
