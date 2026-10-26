import unittest

from solution import (
    count_by_grade,
)


class CountByGradeTests(unittest.TestCase):

    def test_multiple_students_with_varying_grades(
        self,
    ) -> None:
        students: list[dict[str, str]] = [
            {"name": "A", "grade": "pass"},
            {"name": "B", "grade": "fail"},
            {"name": "C", "grade": "pass"},
        ]
        expected_counts: dict[str, int] = {"pass": 2, "fail": 1}

        actual_counts: dict[str, int] = count_by_grade(
            students,
        )

        self.assertEqual(
            actual_counts,
            expected_counts,
        )

    def test_empty_student_roster(
        self,
    ) -> None:
        students: list[dict[str, str]] = []
        expected_counts: dict[str, int] = {}

        actual_counts: dict[str, int] = count_by_grade(
            students,
        )

        self.assertEqual(
            actual_counts,
            expected_counts,
        )


if __name__ == "__main__":
    unittest.main()
