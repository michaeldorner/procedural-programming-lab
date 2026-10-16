import unittest

from solution import factorial


class Exercise12RequiredTests(unittest.TestCase):

    def test_factorial_of_five(
        self,
    ) -> None:
        n: int = 5
        expected_result: int = 120

        actual_result: int = factorial(
            n,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_factorial_of_three(
        self,
    ) -> None:
        n: int = 3
        expected_result: int = 6

        actual_result: int = factorial(
            n,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_factorial_of_one(
        self,
    ) -> None:
        n: int = 1
        expected_result: int = 1

        actual_result: int = factorial(
            n,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
