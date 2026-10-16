import unittest

from solution import (
    average,
)


class Exercise18BonusTests(unittest.TestCase):

    def test_average_1(
        self,
    ) -> None:
        value_0 = [2.5, 3.5]
        expected_result = 3.0

        actual_result = average(
            value_0,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
