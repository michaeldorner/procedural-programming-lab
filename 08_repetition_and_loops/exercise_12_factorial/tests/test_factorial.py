import unittest
from typing import cast

from solution import factorial


class FactorialCalculationTests(unittest.TestCase):

    def test_factorial_of_one(
        self,
    ) -> None:
        number: int = 1
        expected_factorial: int = 1

        actual_factorial: int = factorial(
            number,
        )

        self.assertEqual(
            actual_factorial,
            expected_factorial,
        )

    def test_factorial_of_three(
        self,
    ) -> None:
        number: int = 3
        expected_factorial: int = 6

        actual_factorial: int = factorial(
            number,
        )

        self.assertEqual(
            actual_factorial,
            expected_factorial,
        )

    def test_factorial_of_five(
        self,
    ) -> None:
        number: int = 5
        expected_factorial: int = 120

        actual_factorial: int = factorial(
            number,
        )

        self.assertEqual(
            actual_factorial,
            expected_factorial,
        )

    def test_factorial_of_seven(
        self,
    ) -> None:
        number: int = 7
        expected_factorial: int = 5040

        actual_factorial: int = factorial(
            number,
        )

        self.assertEqual(
            actual_factorial,
            expected_factorial,
        )

    def test_factorial_of_ten(
        self,
    ) -> None:
        number: int = 10
        expected_factorial: int = 3628800

        actual_factorial: int = factorial(
            number,
        )

        self.assertEqual(
            actual_factorial,
            expected_factorial,
        )


class FactorialBoundaryTests(unittest.TestCase):

    def test_factorial_of_zero(
        self,
    ) -> None:
        number: int = 0
        expected_factorial: int = 1

        actual_factorial: int = factorial(
            number,
        )

        self.assertEqual(
            actual_factorial,
            expected_factorial,
        )


class FactorialValidationTests(unittest.TestCase):

    def test_rejects_negative_integer(
        self,
    ) -> None:
        negative_number: int = -1

        with self.assertRaises(
            ValueError,
        ):
            factorial(
                negative_number,
            )

    def test_rejects_boolean_true(
        self,
    ) -> None:
        boolean_value: int = cast(
            int,
            True,
        )

        with self.assertRaises(
            ValueError,
        ):
            factorial(
                boolean_value,
            )

    def test_rejects_float(
        self,
    ) -> None:
        float_value: int = cast(
            int,
            5.0,
        )

        with self.assertRaises(
            ValueError,
        ):
            factorial(
                float_value,
            )


if __name__ == "__main__":
    unittest.main()
