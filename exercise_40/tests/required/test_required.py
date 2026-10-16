import unittest

from solution import (
    OrderStatus,
    is_final,
)


class Exercise40RequiredTests(unittest.TestCase):

    def test_is_final_1(
        self,
    ) -> None:
        value_0 = OrderStatus.OPEN
        expected_result = False

        actual_result = is_final(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_is_final_2(
        self,
    ) -> None:
        value_0 = OrderStatus.SHIPPED
        expected_result = True

        actual_result = is_final(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
