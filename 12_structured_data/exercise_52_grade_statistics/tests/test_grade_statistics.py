import unittest

from solution import (
    grade_statistics,
)


class GradeStatisticsTests(unittest.TestCase):

    def test_multiple_grades_statistics(
        self,
    ) -> None:
        grades: list[float] = [1.0, 2.0, 3.0]
        expected_stats: tuple[float, float, float] = (2.0, 1.0, 3.0)

        actual_stats: tuple[float, float, float] = grade_statistics(
            grades,
        )

        self.assertAlmostEqual(actual_stats[0], expected_stats[0])
        self.assertAlmostEqual(actual_stats[1], expected_stats[1])
        self.assertAlmostEqual(actual_stats[2], expected_stats[2])

    def test_single_grade_statistics(
        self,
    ) -> None:
        grades: list[float] = [2.0]
        expected_stats: tuple[float, float, float] = (2.0, 2.0, 2.0)

        actual_stats: tuple[float, float, float] = grade_statistics(
            grades,
        )

        self.assertAlmostEqual(actual_stats[0], expected_stats[0])
        self.assertAlmostEqual(actual_stats[1], expected_stats[1])
        self.assertAlmostEqual(actual_stats[2], expected_stats[2])


if __name__ == "__main__":
    unittest.main()
