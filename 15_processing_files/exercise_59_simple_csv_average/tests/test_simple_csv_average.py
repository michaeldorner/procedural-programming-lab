import os
import tempfile
import unittest

from solution import (
    simple_csv_average,
)


class CsvAverageTests(unittest.TestCase):

    def test_multiple_rows_column_average(
        self,
    ) -> None:
        csv_content: str = "name,grade\nAda,1.0\nAlan,3.0\nGrace,2.0\n"
        column_index: int = 1
        expected_average: float = 2.0

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(csv_content)
            file_path: str = temporary_file.name

        try:
            actual_average: float = simple_csv_average(
                file_path,
                column_index,
            )
            self.assertAlmostEqual(
                actual_average,
                expected_average,
            )
        finally:
            os.remove(file_path)

    def test_single_row_column_average(
        self,
    ) -> None:
        csv_content: str = "name,grade\nAda,2.5\n"
        column_index: int = 1
        expected_average: float = 2.5

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(csv_content)
            file_path: str = temporary_file.name

        try:
            actual_average: float = simple_csv_average(
                file_path,
                column_index,
            )
            self.assertAlmostEqual(
                actual_average,
                expected_average,
            )
        finally:
            os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
