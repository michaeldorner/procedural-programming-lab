import unittest

from solution import (
    GradeLevel,
    grade_level,
)


class GradeLevelClassificationTests(unittest.TestCase):

    def test_excellent_score(
        self,
    ) -> None:
        score: int = 95
        expected_level: GradeLevel = GradeLevel.EXCELLENT

        actual_level: GradeLevel = grade_level(
            score,
        )

        self.assertEqual(
            actual_level,
            expected_level,
        )

    def test_good_score(
        self,
    ) -> None:
        score: int = 85
        expected_level: GradeLevel = GradeLevel.GOOD

        actual_level: GradeLevel = grade_level(
            score,
        )

        self.assertEqual(
            actual_level,
            expected_level,
        )

    def test_pass_score(
        self,
    ) -> None:
        score: int = 65
        expected_level: GradeLevel = GradeLevel.PASS

        actual_level: GradeLevel = grade_level(
            score,
        )

        self.assertEqual(
            actual_level,
            expected_level,
        )

    def test_fail_score(
        self,
    ) -> None:
        score: int = 45
        expected_level: GradeLevel = GradeLevel.FAIL

        actual_level: GradeLevel = grade_level(
            score,
        )

        self.assertEqual(
            actual_level,
            expected_level,
        )


if __name__ == "__main__":
    unittest.main()
