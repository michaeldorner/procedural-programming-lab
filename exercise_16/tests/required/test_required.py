import unittest

from solution import (
    gcd,
)


class Exercise16RequiredTests(unittest.TestCase):

    def test_gcd_1(
        self,
    ) -> None:
        value_0 = 12
        value_1 = 8
        expected_result = 4

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
