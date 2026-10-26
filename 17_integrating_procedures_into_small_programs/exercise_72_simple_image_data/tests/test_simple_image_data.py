import unittest

from solution import (
    average_brightness,
    count_dark_pixels,
)


class SimpleImageDataTests(unittest.TestCase):

    def test_average_brightness_calculation(
        self,
    ) -> None:
        image_path: str = "data/simple_image.ppm"
        expected_brightness: float = 0.5

        actual_brightness: float = average_brightness(
            image_path,
        )

        self.assertAlmostEqual(
            actual_brightness,
            expected_brightness,
        )

    def test_count_dark_pixels_below_threshold(
        self,
    ) -> None:
        image_path: str = "data/simple_image.ppm"
        brightness_threshold: float = 0.5
        expected_count: int = 1

        actual_count: int = count_dark_pixels(
            image_path,
            brightness_threshold,
        )

        self.assertEqual(
            actual_count,
            expected_count,
        )


if __name__ == "__main__":
    unittest.main()
