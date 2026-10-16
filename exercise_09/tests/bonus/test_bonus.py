import unittest
from typing import cast

from solution import minimum_of_three


class Exercise09BonusTests(unittest.TestCase):

    def test_all_values_are_equal(
        self,
    ) -> None:
        a: int = 7
        b: int = 7
        c: int = 7
        expected_result: int = 7

        actual_result: int = minimum_of_three(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_negative_values(
        self,
    ) -> None:
        a: int = -1
        b: int = -5
        c: int = 0
        expected_result: int = -5

        actual_result: int = minimum_of_three(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_duplicate_minimum_values(
        self,
    ) -> None:
        a: int = 4
        b: int = 2
        c: int = 2
        expected_result: int = 2

        actual_result: int = minimum_of_three(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_zero_is_minimum(
        self,
    ) -> None:
        a: int = 5
        b: int = 0
        c: int = 3
        expected_result: int = 0

        actual_result: int = minimum_of_three(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_boolean_first_value_is_rejected(
        self,
    ) -> None:
        a = cast(
            int,
            True,
        )
        b: int = 1
        c: int = 2

        with self.assertRaises(ValueError):
            minimum_of_three(
                a,
                b,
                c,
            )

    def test_boolean_second_value_is_rejected(
        self,
    ) -> None:
        a: int = 1
        b = cast(
            int,
            False,
        )
        c: int = 2

        with self.assertRaises(ValueError):
            minimum_of_three(
                a,
                b,
                c,
            )

    def test_float_is_rejected(
        self,
    ) -> None:
        a: int = 1
        b = cast(
            int,
            2.5,
        )
        c: int = 3

        with self.assertRaises(ValueError):
            minimum_of_three(
                a,
                b,
                c,
            )

    def test_string_is_rejected(
        self,
    ) -> None:
        a: int = 1
        b: int = 2
        c = cast(
            int,
            "3",
        )

        with self.assertRaises(ValueError):
            minimum_of_three(
                a,
                b,
                c,
            )


if __name__ == "__main__":
    unittest.main()
