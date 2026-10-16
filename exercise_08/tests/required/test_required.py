import unittest

from solution import is_leap_year


class Exercise08RequiredTests(unittest.TestCase):

    def test_leap_year_divisible_by_four(
        self,
    ) -> None:
        year: int = 2024
        expected_result: bool = True

        actual_result: bool = is_leap_year(
            year,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_common_year_not_divisible_by_four(
        self,
    ) -> None:
        year: int = 2023
        expected_result: bool = False

        actual_result: bool = is_leap_year(
            year,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
