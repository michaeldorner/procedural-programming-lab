import unittest

from solution import (
    gcd,
)


class Exercise16BonusTests(unittest.TestCase):

    def test_gcd_1(
        self,
    ) -> None:
        value_0 = 54
        value_1 = 24
        expected_result = 6

        actual_result = gcd(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
