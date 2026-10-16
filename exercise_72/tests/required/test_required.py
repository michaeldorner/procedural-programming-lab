import unittest

from solution import (
    _read_pixel_brightness_values,
    average_brightness,
    count_dark_pixels,
)


class Exercise72RequiredTests(unittest.TestCase):

    def test_average_brightness_1(
        self,
    ) -> None:
        value_0 = 'data/simple_image.ppm'
        expected_result = 0.5

        actual_result = average_brightness(
            value_0,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
