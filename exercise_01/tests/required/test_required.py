import unittest

from solution import (
    rectangle_area,
    rectangle_perimeter,
)


class Exercise01RequiredTests(unittest.TestCase):

    def test_rectangle_area_1(
        self,
    ) -> None:
        value_0 = 3.0
        value_1 = 4.0
        expected_result = 12.0

        actual_result = rectangle_area(
            value_0,
            value_1,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )

    def test_rectangle_perimeter_2(
        self,
    ) -> None:
        value_0 = 3.0
        value_1 = 4.0
        expected_result = 14.0

        actual_result: float = rectangle_perimeter(
            value_0,
            value_1,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
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
