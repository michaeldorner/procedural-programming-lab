import unittest
from typing import cast

from solution import sum_between


class TypicalRangeSumTests(unittest.TestCase):

    def test_sum_from_one_to_five(
        self,
    ) -> None:
        start: int = 1
        end: int = 5
        expected_sum: int = 15

        actual_sum: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )

    def test_sum_from_three_to_six(
        self,
    ) -> None:
        start: int = 3
        end: int = 6
        expected_sum: int = 18

        actual_sum: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )

    def test_sum_spanning_negative_and_positive(
        self,
    ) -> None:
        start: int = -3
        end: int = 3
        expected_sum: int = 0

        actual_sum: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )

    def test_sum_negative_range(
        self,
    ) -> None:
        start: int = -5
        end: int = -1
        expected_sum: int = -15

        actual_sum: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )

    def test_sum_large_range(
        self,
    ) -> None:
        start: int = 1
        end: int = 100
        expected_sum: int = 5050

        actual_sum: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )


class BoundaryRangeSumTests(unittest.TestCase):

    def test_single_value_positive(
        self,
    ) -> None:
        start: int = 5
        end: int = 5
        expected_sum: int = 5

        actual_sum: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )

    def test_single_value_zero(
        self,
    ) -> None:
        start: int = 0
        end: int = 0
        expected_sum: int = 0

        actual_sum: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_sum,
            expected_sum,
        )


class SumBetweenValidationTests(unittest.TestCase):

    def test_rejects_start_greater_than_end(
        self,
    ) -> None:
        start: int = 5
        end: int = 1

        with self.assertRaises(
            ValueError,
        ):
            sum_between(
                start,
                end,
            )

    def test_rejects_boolean_start(
        self,
    ) -> None:
        boolean_start = cast(
            int,
            True,
        )
        end: int = 5

        with self.assertRaises(
            ValueError,
        ):
            sum_between(
                boolean_start,
                end,
            )

    def test_rejects_boolean_end(
        self,
    ) -> None:
        start: int = 1
        boolean_end = cast(
            int,
            False,
        )

        with self.assertRaises(
            ValueError,
        ):
            sum_between(
                start,
                boolean_end,
            )

    def test_rejects_float_start(
        self,
    ) -> None:
        float_start = cast(
            int,
            1.5,
        )
        end: int = 5

        with self.assertRaises(
            ValueError,
        ):
            sum_between(
                float_start,
                end,
            )

    def test_rejects_float_end(
        self,
    ) -> None:
        start: int = 1
        float_end = cast(
            int,
            5.5,
        )

        with self.assertRaises(
            ValueError,
        ):
            sum_between(
                start,
                float_end,
            )


if __name__ == "__main__":
    unittest.main()
