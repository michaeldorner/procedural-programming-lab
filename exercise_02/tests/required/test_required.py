import unittest

from solution import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)


class Exercise02RequiredTests(unittest.TestCase):

    def test_celsius_to_fahrenheit_freezing_point(
        self,
    ) -> None:
        celsius = 0.0
        expected_fahrenheit = 32.0

        actual_fahrenheit = celsius_to_fahrenheit(
            celsius,
        )

        self.assertEqual(
            actual_fahrenheit,
            expected_fahrenheit,
        )

    def test_fahrenheit_to_celsius_boiling_point(
        self,
    ) -> None:
        fahrenheit = 212.0
        expected_celsius = 100.0

        actual_celsius = fahrenheit_to_celsius(
            fahrenheit,
        )

        self.assertEqual(
            actual_celsius,
            expected_celsius,
        )


if __name__ == "__main__":
    unittest.main()
