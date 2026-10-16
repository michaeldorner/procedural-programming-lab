import unittest

from solution import (
    _read_pixel_brightness_values,
    average_brightness,
    count_dark_pixels,
)


class Exercise72BonusTests(unittest.TestCase):

    def test_count_dark_pixels_1(
        self,
    ) -> None:
        value_0 = 'data/simple_image.ppm'
        value_1 = 0.5
        expected_result = 1

        actual_result = count_dark_pixels(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
