import tempfile
import unittest

from solution import csv_grade_statistics


class Exercise60RequiredTests(unittest.TestCase):

    def test_csv_grade_statistics(
        self,
    ) -> None:
        content = 'name,grade\nAda,1.0\nAlan,3.0\nGrace,2.0\n'
        expected_result = (2.0, 1.0, 3.0)

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as file:
            file.write(content)
            filename = file.name

        actual_result = csv_grade_statistics(
            filename,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
