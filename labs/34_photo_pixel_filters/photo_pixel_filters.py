"""Lab 34: Photo Pixel Filters."""

Pixel = tuple[int, int, int]
Image = list[list[Pixel]]


def to_grayscale(image: Image) -> Image:
    """Convert an RGB image to luminance grayscale."""
    result: Image = []
    for row in image:
        new_row: list[Pixel] = []
        for r, g, b in row:
            y: int = int(0.299 * r + 0.587 * g + 0.114 * b)
            new_row.append((y, y, y))
        result.append(new_row)
    return result


def adjust_brightness(image: Image, delta: int) -> Image:
    """Shift every RGB channel by delta, clamped to [0, 255]."""
    def _clamp(val: int) -> int:
        return max(0, min(255, val))

    return [
        [(_clamp(r + delta), _clamp(g + delta), _clamp(b + delta)) for r, g, b in row]
        for row in image
    ]


def rotate_90_cw(image: Image) -> Image:
    """Rotate a non-empty rectangular RGB image 90 degrees clockwise."""
    if not image or not image[0]:
        return []
    rows: int = len(image)
    cols: int = len(image[0])
    return [[image[rows - 1 - r][c] for r in range(rows)] for c in range(cols)]


def encode_ppm_p6(image: Image) -> bytes:
    """Encode an RGB image as binary PPM (P6)."""
    height: int = len(image)
    width: int = len(image[0]) if height > 0 else 0
    header: bytes = f"P6\n{width} {height}\n255\n".encode("ascii")
    payload = bytearray()
    for row in image:
        for r, g, b in row:
            payload.extend((r, g, b))
    return header + bytes(payload)


if __name__ == "__main__":
    img: Image = [[(255, 0, 0), (0, 255, 0)]]
    print("P6 bytes:", encode_ppm_p6(rotate_90_cw(img)))
