import unittest

from solution import (
    calculate_rectangle_area,
    calculate_rectangle_perimeter,
)


class RectangleAreaTests(unittest.TestCase):

    def test_regular_rectangle(
        self,
    ) -> None:
        # Arrange
        width: float = 3.0
        height: float = 4.0
        expected_area: float = 12.0

        # Act
        actual_area: float = calculate_rectangle_area(
            width,
            height,
        )

        # Assert
        self.assertAlmostEqual(
            actual_area,
            expected_area,
        )

    def test_float_dimensions(
        self,
    ) -> None:
        # Arrange
        width: float = 1.5
        height: float = 2.0
        expected_area: float = 3.0

        # Act
        actual_area: float = calculate_rectangle_area(
            width,
            height,
        )

        # Assert
        self.assertAlmostEqual(
            actual_area,
            expected_area,
        )

    def test_zero_width(
        self,
    ) -> None:
        # Arrange
        width: float = 0.0
        height: float = 5.0
        expected_area: float = 0.0

        # Act
        actual_area: float = calculate_rectangle_area(
            width,
            height,
        )

        # Assert
        self.assertAlmostEqual(
            actual_area,
            expected_area,
        )

    def test_zero_height(
        self,
    ) -> None:
        # Arrange
        width: float = 5.0
        height: float = 0.0
        expected_area: float = 0.0

        # Act
        actual_area: float = calculate_rectangle_area(
            width,
            height,
        )

        # Assert
        self.assertAlmostEqual(
            actual_area,
            expected_area,
        )


class RectanglePerimeterTests(unittest.TestCase):

    def test_regular_rectangle(
        self,
    ) -> None:
        # Arrange
        width: float = 3.0
        height: float = 4.0
        expected_perimeter: float = 14.0

        # Act
        actual_perimeter: float = (
            calculate_rectangle_perimeter(
                width,
                height,
            )
        )

        # Assert
        self.assertAlmostEqual(
            actual_perimeter,
            expected_perimeter,
        )

    def test_float_dimensions(
        self,
    ) -> None:
        # Arrange
        width: float = 1.5
        height: float = 2.0
        expected_perimeter: float = 7.0

        # Act
        actual_perimeter: float = (
            calculate_rectangle_perimeter(
                width,
                height,
            )
        )

        # Assert
        self.assertAlmostEqual(
            actual_perimeter,
            expected_perimeter,
        )

    def test_zero_width(
        self,
    ) -> None:
        # Arrange
        width: float = 0.0
        height: float = 5.0
        expected_perimeter: float = 10.0

        # Act
        actual_perimeter: float = (
            calculate_rectangle_perimeter(
                width,
                height,
            )
        )

        # Assert
        self.assertAlmostEqual(
            actual_perimeter,
            expected_perimeter,
        )

    def test_zero_height(
        self,
    ) -> None:
        # Arrange
        width: float = 5.0
        height: float = 0.0
        expected_perimeter: float = 10.0

        # Act
        actual_perimeter: float = (
            calculate_rectangle_perimeter(
                width,
                height,
            )
        )

        # Assert
        self.assertAlmostEqual(
            actual_perimeter,
            expected_perimeter,
        )


class RectangleValidationTests(unittest.TestCase):

    def test_area_rejects_negative_width(
        self,
    ) -> None:
        # Arrange
        width: float = -1.0
        height: float = 5.0

        # Act and Assert
        with self.assertRaises(
            ValueError,
        ):
            calculate_rectangle_area(
                width,
                height,
            )

    def test_area_rejects_negative_height(
        self,
    ) -> None:
        # Arrange
        width: float = 5.0
        height: float = -1.0

        # Act and Assert
        with self.assertRaises(
            ValueError,
        ):
            calculate_rectangle_area(
                width,
                height,
            )

    def test_perimeter_rejects_negative_width(
        self,
    ) -> None:
        # Arrange
        width: float = -1.0
        height: float = 5.0

        # Act and Assert
        with self.assertRaises(
            ValueError,
        ):
            calculate_rectangle_perimeter(
                width,
                height,
            )

    def test_perimeter_rejects_negative_height(
        self,
    ) -> None:
        # Arrange
        width: float = 5.0
        height: float = -1.0

        # Act and Assert
        with self.assertRaises(
            ValueError,
        ):
            calculate_rectangle_perimeter(
                width,
                height,
            )


if __name__ == "__main__":
    unittest.main()
