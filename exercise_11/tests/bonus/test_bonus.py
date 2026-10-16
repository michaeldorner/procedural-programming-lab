import unittest
from typing import cast

from solution import sum_between


class Exercise11BonusTests(unittest.TestCase):

    def test_sum_between_zero_and_zero(
        self,
    ) -> None:
        start: int = 0
        end: int = 0
        expected_result: int = 0

        actual_result: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_sum_between_negative_and_positive_values(
        self,
    ) -> None:
        start: int = -3
        end: int = 3
        expected_result: int = 0

        actual_result: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_sum_between_negative_values(
        self,
    ) -> None:
        start: int = -5
        end: int = -1
        expected_result: int = -15

        actual_result: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_sum_between_large_range(
        self,
    ) -> None:
        start: int = 1
        end: int = 100
        expected_result: int = 5050

        actual_result: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_start_greater_than_end_is_rejected(
        self,
    ) -> None:
        start: int = 5
        end: int = 1

        with self.assertRaises(ValueError):
            sum_between(
                start,
                end,
            )

    def test_boolean_start_is_rejected(
        self,
    ) -> None:
        start = cast(
            int,
            True,
        )
        end: int = 5

        with self.assertRaises(ValueError):
            sum_between(
                start,
                end,
            )

    def test_boolean_end_is_rejected(
        self,
    ) -> None:
        start: int = 1
        end = cast(
            int,
            False,
        )

        with self.assertRaises(ValueError):
            sum_between(
                start,
                end,
            )

    def test_float_start_is_rejected(
        self,
    ) -> None:
        start = cast(
            int,
            1.5,
        )
        end: int = 5

        with self.assertRaises(ValueError):
            sum_between(
                start,
                end,
            )

    def test_float_end_is_rejected(
        self,
    ) -> None:
        start: int = 1
        end = cast(
            int,
            5.5,
        )

        with self.assertRaises(ValueError):
            sum_between(
                start,
                end,
            )

    def test_string_start_is_rejected(
        self,
    ) -> None:
        start = cast(
            int,
            "1",
        )
        end: int = 5

        with self.assertRaises(ValueError):
            sum_between(
                start,
                end,
            )


if __name__ == "__main__":
    unittest.main()
