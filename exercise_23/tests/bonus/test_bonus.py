import unittest

from solution import (
    filter_even,
)


class Exercise23BonusTests(unittest.TestCase):

    def test_filter_even_1(
        self,
    ) -> None:
        value_0 = [-2, -1, 0]
        expected_result = [-2, 0]

        actual_result = filter_even(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
