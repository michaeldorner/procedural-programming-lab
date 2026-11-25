"""Unit tests for prime_factorization."""

import unittest

from prime_factorization import is_prime, prime_factors


class TestPrimeFactorization(unittest.TestCase):
    """Tests for prime_factors and is_prime."""

    def test_prime_factors(self) -> None:
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(84), [2, 2, 3, 7])
        self.assertEqual(prime_factors(97), [97])
        with self.assertRaises(ValueError):
            prime_factors(1)

    def test_is_prime(self) -> None:
        self.assertIs(is_prime(1), False)
        self.assertIs(is_prime(2), True)
        self.assertIs(is_prime(29), True)
        self.assertIs(is_prime(49), False)
