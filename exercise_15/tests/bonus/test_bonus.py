import unittest

from solution import (
    is_prime,
)


class Exercise15BonusTests(unittest.TestCase):

    def test_is_prime_1(
        self,
    ) -> None:
        value_0 = 97
        expected_result = True

        actual_result = is_prime(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
