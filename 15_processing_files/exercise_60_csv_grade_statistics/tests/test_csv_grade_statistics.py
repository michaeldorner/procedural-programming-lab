import os
import tempfile
import unittest

from solution import (
    csv_grade_statistics,
)


class CsvGradeStatisticsTests(unittest.TestCase):

    def test_multiple_students_grade_statistics(
        self,
    ) -> None:
        csv_content: str = "name,grade\nAda,1.0\nAlan,3.0\nGrace,2.0\n"
        expected_statistics: tuple[float, float, float] = (2.0, 1.0, 3.0)

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(csv_content)
            file_path: str = temporary_file.name

        try:
            actual_statistics: tuple[
                float, float, float
            ] = csv_grade_statistics(
                file_path,
            )
            self.assertAlmostEqual(
                actual_statistics[0],
                expected_statistics[0],
            )
            self.assertAlmostEqual(
                actual_statistics[1],
                expected_statistics[1],
            )
            self.assertAlmostEqual(
                actual_statistics[2],
                expected_statistics[2],
            )
        finally:
            os.remove(file_path)

    def test_single_student_grade_statistics(
        self,
    ) -> None:
        csv_content: str = "name,grade\nAda,2.5\n"
        expected_statistics: tuple[float, float, float] = (2.5, 2.5, 2.5)

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(csv_content)
            file_path: str = temporary_file.name

        try:
            actual_statistics: tuple[
                float, float, float
            ] = csv_grade_statistics(
                file_path,
            )
            self.assertAlmostEqual(
                actual_statistics[0],
                expected_statistics[0],
            )
            self.assertAlmostEqual(
                actual_statistics[1],
                expected_statistics[1],
            )
            self.assertAlmostEqual(
                actual_statistics[2],
                expected_statistics[2],
            )
        finally:
            os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
