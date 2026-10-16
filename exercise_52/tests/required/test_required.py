import unittest

from solution import (
    grade_statistics,
)


class Exercise52RequiredTests(unittest.TestCase):

    def test_grade_statistics_1(
        self,
    ) -> None:
        value_0 = [1.0, 2.0, 3.0]
        expected_result = (2.0, 1.0, 3.0)

        actual_result = grade_statistics(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
