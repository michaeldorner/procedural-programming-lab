import unittest

from solution import (
    average,
)


class Exercise18RequiredTests(unittest.TestCase):

    def test_average_1(
        self,
    ) -> None:
        value_0 = [1.0, 2.0, 3.0]
        expected_result = 2.0

        actual_result = average(
            value_0,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
