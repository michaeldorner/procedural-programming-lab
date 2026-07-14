import unittest

from solution import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)


class Exercise02BonusTests(unittest.TestCase):

    def test_negative_celsius_temperature(self) -> None:
        celsius = -40.0
        expected_fahrenheit = -40.0

        actual_fahrenheit = celsius_to_fahrenheit(
            celsius,
        )

        self.assertEqual(
            actual_fahrenheit,
            expected_fahrenheit,
        )

    def test_negative_fahrenheit_temperature(self) -> None:
        fahrenheit = -40.0
        expected_celsius = -40.0

        actual_celsius = fahrenheit_to_celsius(
            fahrenheit,
        )

        self.assertEqual(
            actual_celsius,
            expected_celsius,
        )

    def test_decimal_celsius_temperature(self) -> None:
        celsius = 20.5
        expected_fahrenheit = 68.9

        actual_fahrenheit = celsius_to_fahrenheit(
            celsius,
        )

        self.assertAlmostEqual(
            actual_fahrenheit,
            expected_fahrenheit,
        )

    def test_decimal_fahrenheit_temperature(self) -> None:
        fahrenheit = 68.9
        expected_celsius = 20.5

        actual_celsius = fahrenheit_to_celsius(
            fahrenheit,
        )

        self.assertAlmostEqual(
            actual_celsius,
            expected_celsius,
        )


if __name__ == "__main__":
    unittest.main()
