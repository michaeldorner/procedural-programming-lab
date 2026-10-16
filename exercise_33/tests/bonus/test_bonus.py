import unittest

from solution import (
    student_average,
)


class Exercise33BonusTests(unittest.TestCase):

    def test_student_average_1(
        self,
    ) -> None:
        value_0 = {'Ada': 1.5, 'Alan': 2.5, 'Grace': 2.0}
        expected_result = 2.0

        actual_result = student_average(
            value_0,
        )

        self.assertAlmostEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
