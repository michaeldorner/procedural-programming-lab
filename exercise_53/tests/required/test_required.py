import unittest

from solution import (
    shopping_cart_total,
)


class Exercise53RequiredTests(unittest.TestCase):

    def test_shopping_cart_total_1(
        self,
    ) -> None:
        value_0 = {'apple': 2}
        value_1 = {'apple': 1.5}
        expected_result = 3.0

        actual_result = shopping_cart_total(
            value_0,
            value_1,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
