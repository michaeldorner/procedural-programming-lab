import unittest

from solution import (
    count_by_grade,
)


class Exercise51BonusTests(unittest.TestCase):

    def test_count_by_grade_1(
        self,
    ) -> None:
        value_0 = []
        expected_result = {}

        actual_result = count_by_grade(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
