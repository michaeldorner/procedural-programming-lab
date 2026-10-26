import unittest
from typing import cast

from solution import is_even


class EvenParityTests(unittest.TestCase):

    def test_positive_even_number(
        self,
    ) -> None:
        candidate: int = 4

        parity_result: bool = is_even(
            candidate,
        )

        self.assertTrue(
            parity_result,
        )

    def test_zero_is_even(
        self,
    ) -> None:
        candidate: int = 0

        parity_result: bool = is_even(
            candidate,
        )

        self.assertTrue(
            parity_result,
        )

    def test_negative_even_number(
        self,
    ) -> None:
        candidate: int = -2

        parity_result: bool = is_even(
            candidate,
        )

        self.assertTrue(
            parity_result,
        )

    def test_large_even_number(
        self,
    ) -> None:
        candidate: int = 1_000_000

        parity_result: bool = is_even(
            candidate,
        )

        self.assertTrue(
            parity_result,
        )


class OddParityTests(unittest.TestCase):

    def test_positive_odd_number(
        self,
    ) -> None:
        candidate: int = 5

        parity_result: bool = is_even(
            candidate,
        )

        self.assertFalse(
            parity_result,
        )

    def test_negative_odd_number(
        self,
    ) -> None:
        candidate: int = -3

        parity_result: bool = is_even(
            candidate,
        )

        self.assertFalse(
            parity_result,
        )


class IntegerValidationTests(unittest.TestCase):

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
            is_even(
                boolean_value,
            )

    def test_rejects_boolean_false(
        self,
    ) -> None:
        boolean_value: int = cast(
            int,
            False,
        )

        with self.assertRaises(
            ValueError,
        ):
            is_even(
                boolean_value,
            )

    def test_rejects_float_value(
        self,
    ) -> None:
        float_value: int = cast(
            int,
            2.0,
        )

        with self.assertRaises(
            ValueError,
        ):
            is_even(
                float_value,
            )


if __name__ == "__main__":
    unittest.main()
