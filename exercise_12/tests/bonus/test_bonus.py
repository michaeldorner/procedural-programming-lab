import unittest
from typing import cast

from solution import factorial


class Exercise12BonusTests(unittest.TestCase):

    def test_factorial_of_zero(
        self,
    ) -> None:
        n: int = 0
        expected_result: int = 1

        actual_result: int = factorial(
            n,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_factorial_of_seven(
        self,
    ) -> None:
        n: int = 7
        expected_result: int = 5040

        actual_result: int = factorial(
            n,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_factorial_of_ten(
        self,
    ) -> None:
        n: int = 10
        expected_result: int = 3628800

        actual_result: int = factorial(
            n,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_negative_number_is_rejected(
        self,
    ) -> None:
        n: int = -1

        with self.assertRaises(ValueError):
            factorial(
                n,
            )

    def test_boolean_true_is_rejected(
        self,
    ) -> None:
        n = cast(
            int,
            True,
        )

        with self.assertRaises(ValueError):
            factorial(
                n,
            )

    def test_boolean_false_is_rejected(
        self,
    ) -> None:
        n = cast(
            int,
            False,
        )

        with self.assertRaises(ValueError):
            factorial(
                n,
            )

    def test_float_is_rejected(
        self,
    ) -> None:
        n = cast(
            int,
            5.0,
        )

        with self.assertRaises(ValueError):
            factorial(
                n,
            )

    def test_string_is_rejected(
        self,
    ) -> None:
        n = cast(
            int,
            "5",
        )

        with self.assertRaises(ValueError):
            factorial(
                n,
            )


if __name__ == "__main__":
    unittest.main()
