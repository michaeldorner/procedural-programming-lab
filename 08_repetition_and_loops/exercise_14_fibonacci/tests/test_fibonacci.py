import unittest

from solution import (
    fibonacci,
)


class FibonacciCalculationTests(unittest.TestCase):

    def test_zeroth_fibonacci_number(
        self,
    ) -> None:
        index: int = 0
        expected_value: int = 0

        actual_value: int = fibonacci(
            index,
        )

        self.assertEqual(
            actual_value,
            expected_value,
        )

    def test_seventh_fibonacci_number(
        self,
    ) -> None:
        index: int = 7
        expected_value: int = 13

        actual_value: int = fibonacci(
            index,
        )

        self.assertEqual(
            actual_value,
            expected_value,
        )

    def test_tenth_fibonacci_number(
        self,
    ) -> None:
        index: int = 10
        expected_value: int = 55

        actual_value: int = fibonacci(
            index,
        )

        self.assertEqual(
            actual_value,
            expected_value,
        )


if __name__ == "__main__":
    unittest.main()
