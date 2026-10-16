import unittest

from solution import (
    OrderStatus,
    is_final,
)


class Exercise40BonusTests(unittest.TestCase):

    def test_is_final_1(
        self,
    ) -> None:
        value_0 = OrderStatus.CANCELLED
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
