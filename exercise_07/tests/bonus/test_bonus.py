import unittest
from typing import cast

from solution import grade


class Exercise07BonusTests(unittest.TestCase):

    def test_grade_a_lower_boundary(
        self,
    ) -> None:
        score: int = 90
        expected_result: str = "A"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_b_lower_boundary(
        self,
    ) -> None:
        score: int = 80
        expected_result: str = "B"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_c_lower_boundary(
        self,
    ) -> None:
        score: int = 70
        expected_result: str = "C"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_d_lower_boundary(
        self,
    ) -> None:
        score: int = 60
        expected_result: str = "D"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_f_lower_boundary(
        self,
    ) -> None:
        score: int = 0
        expected_result: str = "F"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_upper_boundary(
        self,
    ) -> None:
        score: int = 100
        expected_result: str = "A"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_score_below_zero_is_rejected(
        self,
    ) -> None:
        score: int = -1

        with self.assertRaises(ValueError):
            grade(
                score,
            )

    def test_score_above_one_hundred_is_rejected(
        self,
    ) -> None:
        score: int = 101

        with self.assertRaises(ValueError):
            grade(
                score,
            )

    def test_boolean_true_is_rejected(
        self,
    ) -> None:
        score = cast(
            int,
            True,
        )

        with self.assertRaises(ValueError):
            grade(
                score,
            )

    def test_boolean_false_is_rejected(
        self,
    ) -> None:
        score = cast(
            int,
            False,
        )

        with self.assertRaises(ValueError):
            grade(
                score,
            )

    def test_float_is_rejected(
        self,
    ) -> None:
        score = cast(
            int,
            82.5,
        )

        with self.assertRaises(ValueError):
            grade(
                score,
            )


if __name__ == "__main__":
    unittest.main()
