# Lab 37: Musical Pitch Tuning

**Topics:** Functions, standard library math, binary packing (`struct`), `wave` file I/O  
**Lectures:** 04 (Functions), 08 (Loops), 13 (Text Processing), 15 (File Processing)

Convert between MIDI notes and frequencies, measure tuning deviation in cents, and synthesize mono 16-bit WAV audio.

## Requirements

- Implement `convert_midi_to_hz` using $f = 440 \cdot 2^{(m - 69) / 12}$.
- Implement `calculate_cents_offset` using $1200 \cdot \log_2(f_{\text{measured}} / f_{\text{target}})$, returning no value for non-positive frequencies.
- Implement `synthesize_sine_pcm16` and `write_sine_wav` to generate and save mono 16-bit signed PCM audio.

## Worked Examples

- MIDI 69 corresponds to 440.0 Hz with 0.0 cents offset relative to 440.0 Hz.

## Implementation Hints

- See [`math.log2()`](https://docs.python.org/3/library/math.html#math.log2), [`struct.pack()`](https://docs.python.org/3/library/struct.html#struct.pack), and [`wave.open()`](https://docs.python.org/3/library/wave.html#wave.open).

## Run & Test

```bash
python musical_pitch_tuning.py
python -m unittest
```
