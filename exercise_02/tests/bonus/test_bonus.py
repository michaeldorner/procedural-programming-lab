import unittest

from solution import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)


class Exercise02BonusTests(unittest.TestCase):

    def test_celsius_to_fahrenheit_negative_temperature(
        self,
    ) -> None:
        celsius = -40.0
        expected_fahrenheit = -40.0

        actual_fahrenheit = celsius_to_fahrenheit(
            celsius,
        )

        self.assertEqual(
            actual_fahrenheit,
            expected_fahrenheit,
        )

    def test_fahrenheit_to_celsius_negative_temperature(
        self,
    ) -> None:
        fahrenheit = -40.0
        expected_celsius = -40.0

        actual_celsius = fahrenheit_to_celsius(
            fahrenheit,
        )

        self.assertEqual(
            actual_celsius,
            expected_celsius,
        )

    def test_celsius_to_fahrenheit_decimal_temperature(
        self,
    ) -> None:
        celsius = 20.5
        expected_fahrenheit = 68.9

        actual_fahrenheit = celsius_to_fahrenheit(
            celsius,
        )

        self.assertAlmostEqual(
            actual_fahrenheit,
            expected_fahrenheit,
        )

    def test_fahrenheit_to_celsius_decimal_temperature(
        self,
    ) -> None:
        fahrenheit = 68.9
        expected_celsius = 20.5

        actual_celsius = fahrenheit_to_celsius(
            fahrenheit,
        )

        self.assertAlmostEqual(
            actual_celsius,
            expected_celsius,
        )

    def test_celsius_fahrenheit_roundtrip(
        self,
    ) -> None:
        original_celsius = 37.0

        fahrenheit = celsius_to_fahrenheit(
            original_celsius,
        )

        actual_celsius = fahrenheit_to_celsius(
            fahrenheit,
        )

        self.assertAlmostEqual(
            actual_celsius,
            original_celsius,
        )

    def test_fahrenheit_celsius_roundtrip(
        self,
    ) -> None:
        original_fahrenheit = 98.6

        celsius = fahrenheit_to_celsius(
            original_fahrenheit,
        )

        actual_fahrenheit = celsius_to_fahrenheit(
            celsius,
        )

        self.assertAlmostEqual(
            actual_fahrenheit,
            original_fahrenheit,
        )

    def test_celsius_below_absolute_zero(
        self,
    ) -> None:
        celsius = -300.0

        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(
                celsius,
            )

    def test_fahrenheit_below_absolute_zero(
        self,
    ) -> None:
        fahrenheit = -500.0

        with self.assertRaises(ValueError):
            fahrenheit_to_celsius(
                fahrenheit,
            )

    def test_celsius_nan(
        self,
    ) -> None:
        celsius = float("nan")

        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(
                celsius,
            )

    def test_fahrenheit_nan(
        self,
    ) -> None:
        fahrenheit = float("nan")

        with self.assertRaises(ValueError):
            fahrenheit_to_celsius(
                fahrenheit,
            )

    def test_celsius_infinity(
        self,
    ) -> None:
        celsius = float("inf")

        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(
                celsius,
            )

    def test_fahrenheit_negative_infinity(
        self,
    ) -> None:
        fahrenheit = float("-inf")

        with self.assertRaises(ValueError):
            fahrenheit_to_celsius(
                fahrenheit,
            )


if __name__ == "__main__":
    unittest.main()
