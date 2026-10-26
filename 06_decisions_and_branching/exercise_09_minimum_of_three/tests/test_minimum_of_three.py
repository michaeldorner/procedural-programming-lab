import unittest
from typing import cast

from solution import minimum_of_three


class MinimumCalculationTests(unittest.TestCase):

    def test_minimum_is_first_value(
        self,
    ) -> None:
        first: int = 1
        second: int = 3
        third: int = 2
        expected_minimum: int = 1

        actual_minimum: int = minimum_of_three(
            first,
            second,
            third,
        )

        self.assertEqual(
            actual_minimum,
            expected_minimum,
        )

    def test_minimum_is_second_value(
        self,
    ) -> None:
        first: int = 3
        second: int = 1
        third: int = 2
        expected_minimum: int = 1

        actual_minimum: int = minimum_of_three(
            first,
            second,
            third,
        )

        self.assertEqual(
            actual_minimum,
            expected_minimum,
        )

    def test_minimum_is_third_value(
        self,
    ) -> None:
        first: int = 3
        second: int = 2
        third: int = 1
        expected_minimum: int = 1

        actual_minimum: int = minimum_of_three(
            first,
            second,
            third,
        )

        self.assertEqual(
            actual_minimum,
            expected_minimum,
        )

    def test_all_values_equal(
        self,
    ) -> None:
        first: int = 7
        second: int = 7
        third: int = 7
        expected_minimum: int = 7

        actual_minimum: int = minimum_of_three(
            first,
            second,
            third,
        )

        self.assertEqual(
            actual_minimum,
            expected_minimum,
        )

    def test_negative_values(
        self,
    ) -> None:
        first: int = -5
        second: int = -1
        third: int = -3
        expected_minimum: int = -5

        actual_minimum: int = minimum_of_three(
            first,
            second,
            third,
        )

        self.assertEqual(
            actual_minimum,
            expected_minimum,
        )

    def test_two_values_equal_and_minimum(
        self,
    ) -> None:
        first: int = 2
        second: int = 2
        third: int = 5
        expected_minimum: int = 2

        actual_minimum: int = minimum_of_three(
            first,
            second,
            third,
        )

        self.assertEqual(
            actual_minimum,
            expected_minimum,
        )


class ValueValidationTests(unittest.TestCase):

    def test_rejects_boolean_first_value(
        self,
    ) -> None:
        boolean_first: int = cast(
            int,
            True,
        )
        second: int = 2
        third: int = 3

        with self.assertRaises(
            ValueError,
        ):
            minimum_of_three(
                boolean_first,
                second,
                third,
            )

    def test_rejects_float_second_value(
        self,
    ) -> None:
        first: int = 1
        float_second: int = cast(
            int,
            2.5,
        )
        third: int = 3

        with self.assertRaises(
            ValueError,
        ):
            minimum_of_three(
                first,
                float_second,
                third,
            )

    def test_rejects_float_third_value(
        self,
    ) -> None:
        first: int = 1
        second: int = 2
        float_third: int = cast(
            int,
            3.0,
        )

        with self.assertRaises(
            ValueError,
        ):
            minimum_of_three(
                first,
                second,
                float_third,
            )


if __name__ == "__main__":
    unittest.main()
