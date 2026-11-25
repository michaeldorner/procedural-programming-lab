# Lab 34: Photo Pixel Filters

**Topics:** 2D nested lists, tuples, clamping, `bytes` and `bytearray`  
**Lectures:** 09 (Built-in Collections), 11 (Mutability & Memory), 13 (Text Processing)

Apply pure pixel filters to 2D RGB images and encode them in binary PPM (`P6`) format.

## Requirements

- Implement `convert_to_grayscale` using luminance $Y = \lfloor 0.299 R + 0.587 G + 0.114 B \rfloor$.
- Implement `adjust_brightness` to shift each channel by `delta` clamped to $[0, 255]$, and `rotate_90_cw` to rotate rectangular images 90° clockwise.
- Implement `encode_ppm_p6` to produce a `P6` header followed by raw RGB byte triples.

## Worked Examples

- Brightening (250, 10, 0) by +20 clamps red to (255, 30, 20).

## Implementation Hints

- Use [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray) and `str.encode("ascii")` for the PPM header.

## Run & Test

```bash
python photo_pixel_filters.py
python -m unittest
```
