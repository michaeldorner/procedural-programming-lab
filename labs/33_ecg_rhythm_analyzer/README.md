# Lab 33: ECG Rhythm Analyzer

**Topics:** Lists, indexed loops, list comprehensions, standard library math  
**Lectures:** 08 (Loops), 09 (Built-in Collections), 10 (Collection Processing Patterns)

Detect R-peaks in a sampled ECG signal with a 200 ms refractory period and compute BPM and RMSSD.

## Requirements

- Implement `detect_r_peaks` to locate local maxima at or above `threshold` separated by at least 200 ms.
- Implement `compute_ecg_metrics` to return no value for fewer than 2 peaks, and otherwise return $(\text{BPM}, \text{RMSSD}_{\text{ms}})$ where $\text{RMSSD} = \sqrt{\frac{1}{k-1}\sum (\text{RR}_{j+1} - \text{RR}_j)^2}$ (0.0 for a single RR interval).

## Worked Examples

- Peaks at [100, 350, 600] at 250 Hz give RR intervals [1000.0, 1000.0] ms -> (60.0, 0.0).

## Implementation Hints

- See [`math.sqrt()`](https://docs.python.org/3/library/math.html#math.sqrt) and [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).

## Run & Test

```bash
python ecg_rhythm_analyzer.py
python -m unittest
```
