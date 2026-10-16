import unittest

from solution import (
    multiplication_table,
)


class Exercise13BonusTests(unittest.TestCase):

    def test_multiplication_table_1(
        self,
    ) -> None:
        value_0 = 0
        expected_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        actual_result = multiplication_table(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
