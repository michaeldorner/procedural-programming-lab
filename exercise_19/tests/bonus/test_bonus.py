import unittest

from solution import (
    maximum,
)


class Exercise19BonusTests(unittest.TestCase):

    def test_maximum_1(
        self,
    ) -> None:
        value_0 = [-5, -2, -9]
        expected_result = -2

        actual_result = maximum(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
