import unittest

from solution import (
    grade_statistics,
)


class Exercise52BonusTests(unittest.TestCase):

    def test_grade_statistics_1(
        self,
    ) -> None:
        value_0 = [2.5]
        expected_result = (2.5, 2.5, 2.5)

        actual_result = grade_statistics(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
