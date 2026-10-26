import unittest
from typing import cast

from solution import grade


class GradeClassificationTests(unittest.TestCase):

    def test_grade_a(
        self,
    ) -> None:
        score: int = 95
        expected_grade: str = "A"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )

    def test_grade_b(
        self,
    ) -> None:
        score: int = 82
        expected_grade: str = "B"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )

    def test_grade_f(
        self,
    ) -> None:
        score: int = 58
        expected_grade: str = "F"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )


class GradeBoundaryTests(unittest.TestCase):

    def test_grade_a_lower_boundary(
        self,
    ) -> None:
        score: int = 90
        expected_grade: str = "A"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )

    def test_grade_a_upper_boundary(
        self,
    ) -> None:
        score: int = 100
        expected_grade: str = "A"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )

    def test_grade_b_lower_boundary(
        self,
    ) -> None:
        score: int = 80
        expected_grade: str = "B"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )

    def test_grade_c_lower_boundary(
        self,
    ) -> None:
        score: int = 70
        expected_grade: str = "C"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )

    def test_grade_d_lower_boundary(
        self,
    ) -> None:
        score: int = 60
        expected_grade: str = "D"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )

    def test_grade_f_lower_boundary(
        self,
    ) -> None:
        score: int = 0
        expected_grade: str = "F"

        actual_grade: str = grade(
            score,
        )

        self.assertEqual(
            actual_grade,
            expected_grade,
        )


class ScoreValidationTests(unittest.TestCase):

    def test_rejects_score_below_zero(
        self,
    ) -> None:
        invalid_score: int = -1

        with self.assertRaises(
            ValueError,
        ):
            grade(
                invalid_score,
            )

    def test_rejects_score_above_one_hundred(
        self,
    ) -> None:
        invalid_score: int = 101

        with self.assertRaises(
            ValueError,
        ):
            grade(
                invalid_score,
            )

    def test_rejects_boolean_true(
        self,
    ) -> None:
        boolean_score = cast(
            int,
            True,
        )

        with self.assertRaises(
            ValueError,
        ):
            grade(
                boolean_score,
            )

    def test_rejects_boolean_false(
        self,
    ) -> None:
        boolean_score = cast(
            int,
            False,
        )

        with self.assertRaises(
            ValueError,
        ):
            grade(
                boolean_score,
            )

    def test_rejects_float_score(
        self,
    ) -> None:
        float_score = cast(
            int,
            82.5,
        )

        with self.assertRaises(
            ValueError,
        ):
            grade(
                float_score,
            )


if __name__ == "__main__":
    unittest.main()
