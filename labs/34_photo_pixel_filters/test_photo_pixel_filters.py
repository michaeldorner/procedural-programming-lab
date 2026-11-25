"""Unit tests for photo_pixel_filters."""

import unittest

from photo_pixel_filters import (
    adjust_brightness,
    encode_ppm_p6,
    rotate_90_cw,
    to_grayscale,
)


class TestPhotoPixelFilters(unittest.TestCase):
    """Tests for RGB filters and PPM P6 encoding."""

    def test_filters_and_rotation(self) -> None:
        img = [[(250, 10, 0), (0, 100, 200)]]
        self.assertEqual(adjust_brightness(img, 20), [[(255, 30, 20), (20, 120, 220)]])
        gray = to_grayscale([[(100, 100, 100)]])
        self.assertEqual(gray, [[(100, 100, 100)]])
        rotated = rotate_90_cw(img)
        self.assertEqual(rotated, [[(250, 10, 0)], [(0, 100, 200)]])
        self.assertEqual(encode_ppm_p6([[(1, 2, 3)]]), b"P6\n1 1\n255\n\x01\x02\x03")
