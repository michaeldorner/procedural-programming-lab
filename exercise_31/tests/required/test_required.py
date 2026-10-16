import unittest

from solution import (
    difference,
)


class Exercise31RequiredTests(unittest.TestCase):

    def test_difference_1(
        self,
    ) -> None:
        value_0 = [1, 2, 3]
        value_1 = [2, 4]
        expected_result = {1, 3}

        actual_result = difference(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
