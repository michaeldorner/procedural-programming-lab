import unittest

from solution import (
    fibonacci,
)


class Exercise14BonusTests(unittest.TestCase):

    def test_fibonacci_1(
        self,
    ) -> None:
        value_0 = 10
        expected_result = 55

        actual_result = fibonacci(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
