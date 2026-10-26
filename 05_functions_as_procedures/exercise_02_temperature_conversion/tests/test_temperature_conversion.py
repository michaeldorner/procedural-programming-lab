import unittest

from solution import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)


class CelsiusToFahrenheitTests(unittest.TestCase):

    def test_freezing_point(
        self,
    ) -> None:
        celsius_input: float = 0.0
        expected_fahrenheit: float = 32.0

        actual_fahrenheit: float = celsius_to_fahrenheit(
            celsius_input,
        )

        self.assertAlmostEqual(
            actual_fahrenheit,
            expected_fahrenheit,
        )

    def test_negative_temperature(
        self,
    ) -> None:
        celsius_input: float = -40.0
        expected_fahrenheit: float = -40.0

        actual_fahrenheit: float = celsius_to_fahrenheit(
            celsius_input,
        )

        self.assertAlmostEqual(
            actual_fahrenheit,
            expected_fahrenheit,
        )

    def test_decimal_temperature(
        self,
    ) -> None:
        celsius_input: float = 20.5
        expected_fahrenheit: float = 68.9

        actual_fahrenheit: float = celsius_to_fahrenheit(
            celsius_input,
        )

        self.assertAlmostEqual(
            actual_fahrenheit,
            expected_fahrenheit,
        )


class FahrenheitToCelsiusTests(unittest.TestCase):

    def test_boiling_point(
        self,
    ) -> None:
        fahrenheit_input: float = 212.0
        expected_celsius: float = 100.0

        actual_celsius: float = fahrenheit_to_celsius(
            fahrenheit_input,
        )

        self.assertAlmostEqual(
            actual_celsius,
            expected_celsius,
        )

    def test_negative_temperature(
        self,
    ) -> None:
        fahrenheit_input: float = -40.0
        expected_celsius: float = -40.0

        actual_celsius: float = fahrenheit_to_celsius(
            fahrenheit_input,
        )

        self.assertAlmostEqual(
            actual_celsius,
            expected_celsius,
        )

    def test_decimal_temperature(
        self,
    ) -> None:
        fahrenheit_input: float = 68.9
        expected_celsius: float = 20.5

        actual_celsius: float = fahrenheit_to_celsius(
            fahrenheit_input,
        )

        self.assertAlmostEqual(
            actual_celsius,
            expected_celsius,
        )


class RoundtripConversionTests(unittest.TestCase):

    def test_celsius_to_fahrenheit_and_back(
        self,
    ) -> None:
        original_celsius: float = 37.0

        intermediate_fahrenheit: float = celsius_to_fahrenheit(
            original_celsius,
        )
        converted_back_celsius: float = fahrenheit_to_celsius(
            intermediate_fahrenheit,
        )

        self.assertAlmostEqual(
            converted_back_celsius,
            original_celsius,
        )

    def test_fahrenheit_to_celsius_and_back(
        self,
    ) -> None:
        original_fahrenheit: float = 98.6

        intermediate_celsius: float = fahrenheit_to_celsius(
            original_fahrenheit,
        )
        converted_back_fahrenheit: float = celsius_to_fahrenheit(
            intermediate_celsius,
        )

        self.assertAlmostEqual(
            converted_back_fahrenheit,
            original_fahrenheit,
        )


class TemperatureValidationTests(unittest.TestCase):

    def test_celsius_below_absolute_zero(
        self,
    ) -> None:
        celsius_input: float = -300.0

        with self.assertRaises(
            ValueError,
        ):
            celsius_to_fahrenheit(
                celsius_input,
            )

    def test_fahrenheit_below_absolute_zero(
        self,
    ) -> None:
        fahrenheit_input: float = -500.0

        with self.assertRaises(
            ValueError,
        ):
            fahrenheit_to_celsius(
                fahrenheit_input,
            )

    def test_celsius_nan(
        self,
    ) -> None:
        celsius_input: float = float("nan")

        with self.assertRaises(
            ValueError,
        ):
            celsius_to_fahrenheit(
                celsius_input,
            )

    def test_fahrenheit_nan(
        self,
    ) -> None:
        fahrenheit_input: float = float("nan")

        with self.assertRaises(
            ValueError,
        ):
            fahrenheit_to_celsius(
                fahrenheit_input,
            )

    def test_celsius_positive_infinity(
        self,
    ) -> None:
        celsius_input: float = float("inf")

        with self.assertRaises(
            ValueError,
        ):
            celsius_to_fahrenheit(
                celsius_input,
            )

    def test_fahrenheit_negative_infinity(
        self,
    ) -> None:
        fahrenheit_input: float = float("-inf")

        with self.assertRaises(
            ValueError,
        ):
            fahrenheit_to_celsius(
                fahrenheit_input,
            )


if __name__ == "__main__":
    unittest.main()
