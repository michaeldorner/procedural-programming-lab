import unittest

from solution import (
    student_average,
)


class StudentAverageTests(unittest.TestCase):

    def test_multiple_students_average(
        self,
    ) -> None:
        grades: dict[str, float] = {"Alice": 1.0, "Bob": 3.0}
        expected_average: float = 2.0

        actual_average: float = student_average(
            grades,
        )

        self.assertAlmostEqual(
            actual_average,
            expected_average,
        )

    def test_single_student_average(
        self,
    ) -> None:
        grades: dict[str, float] = {"Alice": 2.5}
        expected_average: float = 2.5

        actual_average: float = student_average(
            grades,
        )

        self.assertAlmostEqual(
            actual_average,
            expected_average,
        )


if __name__ == "__main__":
    unittest.main()
