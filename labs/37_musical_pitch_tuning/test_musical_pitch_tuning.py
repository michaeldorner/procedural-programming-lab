"""Unit tests for musical_pitch_tuning."""

from pathlib import Path
import tempfile
import unittest
import wave

from musical_pitch_tuning import (
    hz_to_cents_offset,
    midi_to_hz,
    synthesize_sine_pcm16,
    write_sine_wav,
)


class TestMusicalPitchTuning(unittest.TestCase):
    """Tests for MIDI, cents, PCM synthesis, and WAV export."""

    def test_midi_and_cents(self) -> None:
        self.assertAlmostEqual(midi_to_hz(69), 440.0)
        self.assertAlmostEqual(midi_to_hz(81), 880.0)
        self.assertAlmostEqual(hz_to_cents_offset(440.0, 440.0), 0.0)  # type: ignore[arg-type]
        self.assertIsNone(hz_to_cents_offset(0.0, 440.0))

    def test_pcm_and_wav(self) -> None:
        with self.assertRaises(ValueError):
            synthesize_sine_pcm16(440.0, 0.1, sample_rate_hz=0)
        pcm = synthesize_sine_pcm16(440.0, 0.1, sample_rate_hz=8000)
        self.assertEqual(len(pcm), 800 * 2)
        with tempfile.TemporaryDirectory() as tmp_dir:
            wav_path = Path(tmp_dir) / "tone.wav"
            write_sine_wav(wav_path, 440.0, 0.05, sample_rate_hz=8000)
            with wave.open(str(wav_path), "rb") as wf:
                self.assertEqual(wf.getnchannels(), 1)
                self.assertEqual(wf.getsampwidth(), 2)
                self.assertEqual(wf.getframerate(), 8000)
                self.assertEqual(wf.getnframes(), 400)
