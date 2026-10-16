import tempfile
import unittest

from solution import word_frequencies_from_file


class Exercise58BonusTests(unittest.TestCase):

    def test_word_frequencies_from_file(
        self,
    ) -> None:
        content = 'hello world hello\n'
        expected_result = {'hello': 2, 'world': 1}

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as file:
            file.write(content)
            filename = file.name

        actual_result = word_frequencies_from_file(
            filename,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
