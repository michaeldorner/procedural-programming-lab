import unittest

from solution import (
    midpoint,
)


class Exercise25BonusTests(unittest.TestCase):

    def test_midpoint_1(
        self,
    ) -> None:
        value_0 = (-1.0, 1.0)
        value_1 = (1.0, 3.0)
        expected_result = (0.0, 2.0)

        actual_result = midpoint(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
