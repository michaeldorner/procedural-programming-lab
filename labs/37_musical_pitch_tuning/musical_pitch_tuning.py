"""Lab 37: Musical Pitch Tuning."""

import math
from pathlib import Path
import struct
import wave


def midi_to_hz(midi_note: int) -> float:
    """Convert MIDI note number to frequency in Hz (A4 = 69 = 440.0 Hz)."""
    return 440.0 * (2.0 ** ((midi_note - 69) / 12.0))


def hz_to_cents_offset(measured_hz: float, target_hz: float) -> float | None:
    """Return tuning deviation in cents, or None if either frequency <= 0.0."""
    if measured_hz <= 0.0 or target_hz <= 0.0:
        return None
    return 1200.0 * math.log2(measured_hz / target_hz)


def synthesize_sine_pcm16(
    freq_hz: float,
    duration_seconds: float,
    sample_rate_hz: int = 44100,
) -> bytes:
    """Synthesize signed 16-bit little-endian PCM sine wave bytes."""
    if sample_rate_hz <= 0:
        raise ValueError(f"sample_rate_hz must be positive, got {sample_rate_hz}")
    num_samples: int = max(0, int(duration_seconds * sample_rate_hz))
    frames = bytearray()
    for idx in range(num_samples):
        sample_val: float = math.sin(2.0 * math.pi * freq_hz * idx / sample_rate_hz)
        int_sample: int = int(round(sample_val * 32767.0))
        frames.extend(struct.pack("<h", int_sample))
    return bytes(frames)


def write_sine_wav(
    output_path: Path,
    freq_hz: float,
    duration_seconds: float,
    sample_rate_hz: int = 44100,
) -> None:
    """Write a mono 16-bit WAV file to output_path."""
    pcm_bytes: bytes = synthesize_sine_pcm16(freq_hz, duration_seconds, sample_rate_hz)
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate_hz)
        wav_file.writeframes(pcm_bytes)


if __name__ == "__main__":
    print("A4 Hz:", midi_to_hz(69), "PCM bytes:", len(synthesize_sine_pcm16(440.0, 0.1)))
