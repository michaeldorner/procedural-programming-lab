import os
import tempfile
import unittest

from solution import (
    word_frequencies_from_file,
)


class FileWordFrequenciesTests(unittest.TestCase):

    def test_word_frequencies_across_file(
        self,
    ) -> None:
        file_content: str = "apple banana apple\n"
        expected_frequencies: dict[str, int] = {"apple": 2, "banana": 1}

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(file_content)
            file_path: str = temporary_file.name

        try:
            actual_frequencies: dict[str, int] = word_frequencies_from_file(
                file_path,
            )
            self.assertEqual(
                actual_frequencies,
                expected_frequencies,
            )
        finally:
            os.remove(file_path)

    def test_empty_file_returns_empty_dict(
        self,
    ) -> None:
        file_content: str = ""
        expected_frequencies: dict[str, int] = {}

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as temporary_file:
            temporary_file.write(file_content)
            file_path: str = temporary_file.name

        try:
            actual_frequencies: dict[str, int] = word_frequencies_from_file(
                file_path,
            )
            self.assertEqual(
                actual_frequencies,
                expected_frequencies,
            )
        finally:
            os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
