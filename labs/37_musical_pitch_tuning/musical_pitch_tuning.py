"""Lab 37: Musical Pitch Tuning."""

from pathlib import Path


def midi_to_hz(midi_note: int) -> float:
    """Convert MIDI note number to frequency in Hz (A4 = 69 = 440.0 Hz)."""
    raise NotImplementedError


def hz_to_cents_offset(measured_hz: float, target_hz: float) -> float | None:
    """Return tuning deviation in cents, or None if either frequency <= 0.0."""
    raise NotImplementedError


def synthesize_sine_pcm16(
    freq_hz: float,
    duration_seconds: float,
    sample_rate_hz: int = 44100,
) -> bytes:
    """Synthesize signed 16-bit little-endian PCM sine wave bytes."""
    raise NotImplementedError


def write_sine_wav(
    output_path: Path,
    freq_hz: float,
    duration_seconds: float,
    sample_rate_hz: int = 44100,
) -> None:
    """Write a mono 16-bit WAV file to output_path."""
    raise NotImplementedError


if __name__ == "__main__":
    print("A4 Hz:", midi_to_hz(69), "PCM bytes:", len(synthesize_sine_pcm16(440.0, 0.1)))
