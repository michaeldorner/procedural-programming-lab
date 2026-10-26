import unittest

from solution import (
    gcd,
)


class GreatestCommonDivisorTests(unittest.TestCase):

    def test_common_factors_of_twelve_and_eight(
        self,
    ) -> None:
        first_number: int = 12
        second_number: int = 8
        expected_gcd: int = 4

        actual_gcd: int = gcd(
            first_number,
            second_number,
        )

        self.assertEqual(
            actual_gcd,
            expected_gcd,
        )

    def test_common_factors_of_fifty_four_and_twenty_four(
        self,
    ) -> None:
        first_number: int = 54
        second_number: int = 24
        expected_gcd: int = 6

        actual_gcd: int = gcd(
            first_number,
            second_number,
        )

        self.assertEqual(
            actual_gcd,
            expected_gcd,
        )


if __name__ == "__main__":
    unittest.main()
