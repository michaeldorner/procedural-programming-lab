import unittest

from solution import (
    shopping_cart_total,
)


class Exercise53BonusTests(unittest.TestCase):

    def test_shopping_cart_total_1(
        self,
    ) -> None:
        value_0 = {'a': 2, 'b': 3}
        value_1 = {'a': 1.0, 'b': 2.0}
        expected_result = 8.0

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
