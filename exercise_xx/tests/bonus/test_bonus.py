import unittest

from solution import (
    bmi,
)


class Exercise05BonusTests(unittest.TestCase):

    def test_bmi_1(
        self,
    ) -> None:
        value_0 = 72.0
        value_1 = 1.8
        expected_result = 22.22222222222222

        actual_result = bmi(
            value_0,
            value_1,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
