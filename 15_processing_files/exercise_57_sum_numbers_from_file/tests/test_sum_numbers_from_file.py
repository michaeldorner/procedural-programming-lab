import os
import tempfile
import unittest

from solution import (
    sum_numbers_from_file,
)


class FileNumberSumTests(unittest.TestCase):

    def test_sum_multiple_float_lines(
        self,
    ) -> None:
        file_content: str = "10.0\n20.5\n"
        expected_sum: float = 30.5

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(file_content)
            file_path: str = temporary_file.name

        try:
            actual_sum: float = sum_numbers_from_file(
                file_path,
            )
            self.assertAlmostEqual(
                actual_sum,
                expected_sum,
            )
        finally:
            os.remove(file_path)

    def test_empty_file_returns_zero(
        self,
    ) -> None:
        file_content: str = ""
        expected_sum: float = 0.0

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(file_content)
            file_path: str = temporary_file.name

        try:
            actual_sum: float = sum_numbers_from_file(
                file_path,
            )
            self.assertAlmostEqual(
                actual_sum,
                expected_sum,
            )
        finally:
            os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
