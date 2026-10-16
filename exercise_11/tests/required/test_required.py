import unittest

from solution import sum_between


class Exercise11RequiredTests(unittest.TestCase):

    def test_sum_between_one_and_five(
        self,
    ) -> None:
        start: int = 1
        end: int = 5
        expected_result: int = 15

        actual_result: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_sum_between_three_and_six(
        self,
    ) -> None:
        start: int = 3
        end: int = 6
        expected_result: int = 18

        actual_result: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_sum_between_same_start_and_end(
        self,
    ) -> None:
        start: int = 5
        end: int = 5
        expected_result: int = 5

        actual_result: int = sum_between(
            start,
            end,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
