import tempfile
import unittest

from solution import count_lines


class Exercise56BonusTests(unittest.TestCase):

    def test_count_lines(
        self,
    ) -> None:
        content = 'alpha\nbeta\n'
        expected_result = 2

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as file:
            file.write(content)
            filename = file.name

        actual_result = count_lines(
            filename,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
