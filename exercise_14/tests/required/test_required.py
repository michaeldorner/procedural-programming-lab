import unittest

from solution import (
    fibonacci,
)


class Exercise14RequiredTests(unittest.TestCase):

    def test_fibonacci_1(
        self,
    ) -> None:
        value_0 = 0
        expected_result = 0

        actual_result = fibonacci(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_fibonacci_2(
        self,
    ) -> None:
        value_0 = 7
        expected_result = 13

        actual_result = fibonacci(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
