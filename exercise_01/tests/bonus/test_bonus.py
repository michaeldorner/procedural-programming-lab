import unittest

from solution import (
    rectangle_area,
    rectangle_perimeter,
)


class Exercise01BonusTests(unittest.TestCase):

    def test_rectangle_area_with_float_values(
        self,
    ) -> None:
        width = 1.5
        height = 2.0
        expected_area = 3.0

        actual_area = rectangle_area(
            width,
            height,
        )

        self.assertEqual(
            actual_area,
            expected_area,
        )

    def test_rectangle_perimeter_with_float_values(
        self,
    ) -> None:
        width = 1.5
        height = 2.0
        expected_perimeter = 7.0

        actual_perimeter = rectangle_perimeter(
            width,
            height,
        )

        self.assertEqual(
            actual_perimeter,
            expected_perimeter,
        )

    def test_rectangle_area_with_zero_width(
        self,
    ) -> None:
        width = 0.0
        height = 5.0
        expected_area = 0.0

        actual_area = rectangle_area(
            width,
            height,
        )

        self.assertEqual(
            actual_area,
            expected_area,
        )

    def test_rectangle_perimeter_with_zero_width(
        self,
    ) -> None:
        width = 0.0
        height = 5.0
        expected_perimeter = 10.0

        actual_perimeter = rectangle_perimeter(
            width,
            height,
        )

        self.assertEqual(
            actual_perimeter,
            expected_perimeter,
        )

    def test_rectangle_area_with_negative_width(
        self,
    ) -> None:
        width = -1.0
        height = 5.0

        with self.assertRaises(ValueError):
            rectangle_area(
                width,
                height,
            )

    def test_rectangle_perimeter_with_negative_height(
        self,
    ) -> None:
        width = 1.0
        height = -5.0

        with self.assertRaises(ValueError):
            rectangle_perimeter(
                width,
                height,
            )


if __name__ == "__main__":
    unittest.main()
