import unittest

from solution import (
    minimum,
)


class Exercise20RequiredTests(unittest.TestCase):

    def test_minimum_1(
        self,
    ) -> None:
        value_0 = [1, 5, 3]
        expected_result = 1

        actual_result = minimum(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
