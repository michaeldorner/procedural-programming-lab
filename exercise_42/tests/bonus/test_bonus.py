import unittest

from solution import (
    GradeLevel,
    grade_level,
)


class Exercise42BonusTests(unittest.TestCase):

    def test_grade_level_1(
        self,
    ) -> None:
        value_0 = 60
        expected_result = GradeLevel.PASS

        actual_result = grade_level(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
