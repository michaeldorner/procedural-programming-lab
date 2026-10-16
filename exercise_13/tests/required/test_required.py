import unittest

from solution import (
    multiplication_table,
)


class Exercise13RequiredTests(unittest.TestCase):

    def test_multiplication_table_1(
        self,
    ) -> None:
        value_0 = 3
        expected_result = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

        actual_result = multiplication_table(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
