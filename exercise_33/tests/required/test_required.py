import unittest

from solution import (
    student_average,
)


class Exercise33RequiredTests(unittest.TestCase):

    def test_student_average_1(
        self,
    ) -> None:
        value_0 = {'Alice': 1.0, 'Bob': 3.0}
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
