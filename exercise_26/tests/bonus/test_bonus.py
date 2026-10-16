import unittest

from solution import (
    swap_values,
)


class Exercise26BonusTests(unittest.TestCase):

    def test_swap_values_1(
        self,
    ) -> None:
        value_0 = -1
        value_1 = 5
        expected_result = (5, -1)

        actual_result = swap_values(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
