"""Unit tests for prime_factorization."""

import unittest

from .prime_factorization import is_prime, factorize_primes


class TestPrimeFactorization(unittest.TestCase):
    """Tests for factorize_primes and is_prime."""

    def test_prime_factors(self) -> None:
        self.assertEqual(factorize_primes(2), [2])
        self.assertEqual(factorize_primes(84), [2, 2, 3, 7])
        self.assertEqual(factorize_primes(97), [97])
        with self.assertRaises(ValueError):
            factorize_primes(1)

    def test_is_prime(self) -> None:
        self.assertIs(is_prime(1), False)
        self.assertIs(is_prime(2), True)
        self.assertIs(is_prime(29), True)
        self.assertIs(is_prime(49), False)
