import unittest

from solution import (
    difference,
)


class Exercise31BonusTests(unittest.TestCase):

    def test_difference_1(
        self,
    ) -> None:
        value_0 = []
        value_1 = [1]
        expected_result = set()

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
