import tempfile
import unittest

from solution import sum_numbers_from_file


class Exercise57RequiredTests(unittest.TestCase):

    def test_sum_numbers_from_file(
        self,
    ) -> None:
        content = '1\n2.5\n3\n'
        expected_result = 6.5

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as file:
            file.write(content)
            filename = file.name

        actual_result = sum_numbers_from_file(
            filename,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
