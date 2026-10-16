import unittest

from solution import (
    list_sum,
)


class Exercise17RequiredTests(unittest.TestCase):

    def test_list_sum_1(
        self,
    ) -> None:
        value_0 = [1, 2, 3]
        expected_result = 6

        actual_result = list_sum(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
