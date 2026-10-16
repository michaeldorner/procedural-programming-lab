import unittest

from solution import (
    minimum,
)


class Exercise20BonusTests(unittest.TestCase):

    def test_minimum_1(
        self,
    ) -> None:
        value_0 = [-5, -2, -9]
        expected_result = -9

        actual_result = minimum(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
