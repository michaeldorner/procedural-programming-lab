import unittest

from solution import (
    OrderStatus,
    is_final,
)


class OrderFinalityTests(unittest.TestCase):

    def test_shipped_status_is_final(
        self,
    ) -> None:
        status: OrderStatus = OrderStatus.SHIPPED

        finality: bool = is_final(
            status,
        )

        self.assertTrue(
            finality,
        )

    def test_cancelled_status_is_final(
        self,
    ) -> None:
        status: OrderStatus = OrderStatus.CANCELLED

        finality: bool = is_final(
            status,
        )

        self.assertTrue(
            finality,
        )

    def test_open_status_is_not_final(
        self,
    ) -> None:
        status: OrderStatus = OrderStatus.OPEN

        finality: bool = is_final(
            status,
        )

        self.assertFalse(
            finality,
        )


if __name__ == "__main__":
    unittest.main()
