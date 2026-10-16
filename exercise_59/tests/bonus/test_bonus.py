import tempfile
import unittest

from solution import simple_csv_average


class Exercise59BonusTests(unittest.TestCase):

    def test_simple_csv_average(
        self,
    ) -> None:
        content = 'name,grade\nAda,1.0\nAlan,3.0\nGrace,2.0\n'
        expected_result = 2.0

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as file:
            file.write(content)
            filename = file.name

        actual_result = simple_csv_average(
            filename,
            1,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
