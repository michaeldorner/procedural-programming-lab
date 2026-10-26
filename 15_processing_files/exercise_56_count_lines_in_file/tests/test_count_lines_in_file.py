import os
import tempfile
import unittest

from solution import (
    count_lines,
)


class FileLineCountTests(unittest.TestCase):

    def test_multiple_lines_file(
        self,
    ) -> None:
        file_content: str = "alpha\nbeta\n"
        expected_line_count: int = 2

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(file_content)
            file_path: str = temporary_file.name

        try:
            actual_line_count: int = count_lines(
                file_path,
            )
            self.assertEqual(
                actual_line_count,
                expected_line_count,
            )
        finally:
            os.remove(file_path)

    def test_empty_file_returns_zero(
        self,
    ) -> None:
        file_content: str = ""
        expected_line_count: int = 0

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(file_content)
            file_path: str = temporary_file.name

        try:
            actual_line_count: int = count_lines(
                file_path,
            )
            self.assertEqual(
                actual_line_count,
                expected_line_count,
            )
        finally:
            os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
