import unittest

from solution import (
    count_by_grade,
)


class Exercise51RequiredTests(unittest.TestCase):

    def test_count_by_grade_1(
        self,
    ) -> None:
        value_0 = [{'name': 'A', 'grade': 'A'}, {'name': 'B', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}]
        expected_result = {'A': 2, 'B': 1}

        actual_result = count_by_grade(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
