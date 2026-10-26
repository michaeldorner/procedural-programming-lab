import unittest

from solution import (
    shopping_cart_total,
)


class ShoppingCartTotalTests(unittest.TestCase):

    def test_cart_with_items(
        self,
    ) -> None:
        cart: dict[str, int] = {"apple": 2, "banana": 1}
        prices: dict[str, float] = {"apple": 10.0, "banana": 5.0}
        expected_total: float = 25.0

        actual_total: float = shopping_cart_total(
            cart,
            prices,
        )

        self.assertAlmostEqual(
            actual_total,
            expected_total,
        )

    def test_empty_cart_returns_zero(
        self,
    ) -> None:
        cart: dict[str, int] = {}
        prices: dict[str, float] = {"apple": 10.0}
        expected_total: float = 0.0

        actual_total: float = shopping_cart_total(
            cart,
            prices,
        )

        self.assertAlmostEqual(
            actual_total,
            expected_total,
        )


if __name__ == "__main__":
    unittest.main()
