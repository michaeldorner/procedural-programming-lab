"""Lab 34: Photo Pixel Filters."""

Pixel = tuple[int, int, int]
Image = list[list[Pixel]]


def convert_to_grayscale(image: Image) -> Image:
    """Convert an RGB image to luminance grayscale."""
    raise NotImplementedError


def adjust_brightness(image: Image, delta: int) -> Image:
    """Shift every RGB channel by delta, clamped to [0, 255]."""
    raise NotImplementedError


def rotate_90_cw(image: Image) -> Image:
    """Rotate a non-empty rectangular RGB image 90 degrees clockwise."""
    raise NotImplementedError


def encode_ppm_p6(image: Image) -> bytes:
    """Encode an RGB image as binary PPM (P6)."""
    raise NotImplementedError


if __name__ == "__main__":
    img: Image = [[(255, 0, 0), (0, 255, 0)]]
    print("P6 bytes:", encode_ppm_p6(rotate_90_cw(img)))
