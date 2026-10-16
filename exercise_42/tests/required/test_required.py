import unittest

from solution import (
    GradeLevel,
    grade_level,
)


class Exercise42RequiredTests(unittest.TestCase):

    def test_grade_level_1(
        self,
    ) -> None:
        value_0 = 95
        expected_result = GradeLevel.EXCELLENT

        actual_result = grade_level(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_level_2(
        self,
    ) -> None:
        value_0 = 75
        expected_result = GradeLevel.GOOD

        actual_result = grade_level(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_level_3(
        self,
    ) -> None:
        value_0 = 55
        expected_result = GradeLevel.FAIL

        actual_result = grade_level(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
