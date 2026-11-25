"""Lab 34: Photo tuple[int, int, int] Filters."""

def convert_to_grayscale(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    """Convert an RGB image to luminance grayscale."""
    raise NotImplementedError


def adjust_brightness(image: list[list[tuple[int, int, int]]], delta: int) -> list[list[tuple[int, int, int]]]:
    """Shift every RGB channel by delta, clamped to [0, 255]."""
    raise NotImplementedError


def rotate_90_cw(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    """Rotate a non-empty rectangular RGB image 90 degrees clockwise."""
    raise NotImplementedError


def encode_ppm_p6(image: list[list[tuple[int, int, int]]]) -> bytes:
    """Encode an RGB image as binary PPM (P6)."""
    raise NotImplementedError


if __name__ == "__main__":
    img: list[list[tuple[int, int, int]]] = [[(255, 0, 0), (0, 255, 0)]]
    print("P6 bytes:", encode_ppm_p6(rotate_90_cw(img)))
