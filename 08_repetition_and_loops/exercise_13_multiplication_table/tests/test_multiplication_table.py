import unittest

from solution import (
    multiplication_table,
)


class MultiplicationTableTests(unittest.TestCase):

    def test_table_for_positive_integer(
        self,
    ) -> None:
        base_number: int = 3
        expected_products: list[int] = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

        actual_products: list[int] = multiplication_table(
            base_number,
        )

        self.assertEqual(
            actual_products,
            expected_products,
        )

    def test_table_for_zero(
        self,
    ) -> None:
        base_number: int = 0
        expected_products: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        actual_products: list[int] = multiplication_table(
            base_number,
        )

        self.assertEqual(
            actual_products,
            expected_products,
        )


if __name__ == "__main__":
    unittest.main()
