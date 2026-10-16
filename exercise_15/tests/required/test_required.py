import unittest

from solution import (
    is_prime,
)


class Exercise15RequiredTests(unittest.TestCase):

    def test_is_prime_1(
        self,
    ) -> None:
        value_0 = 2
        expected_result = True

        actual_result = is_prime(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_is_prime_2(
        self,
    ) -> None:
        value_0 = 9
        expected_result = False

        actual_result = is_prime(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
