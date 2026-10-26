import unittest

from solution import (
    is_prime,
)


class PrimeNumberTests(unittest.TestCase):

    def test_smallest_prime_number(
        self,
    ) -> None:
        candidate: int = 2

        prime_status: bool = is_prime(
            candidate,
        )

        self.assertTrue(
            prime_status,
        )

    def test_odd_composite_number(
        self,
    ) -> None:
        candidate: int = 9

        prime_status: bool = is_prime(
            candidate,
        )

        self.assertFalse(
            prime_status,
        )

    def test_two_digit_prime_number(
        self,
    ) -> None:
        candidate: int = 97

        prime_status: bool = is_prime(
            candidate,
        )

        self.assertTrue(
            prime_status,
        )


if __name__ == "__main__":
    unittest.main()
