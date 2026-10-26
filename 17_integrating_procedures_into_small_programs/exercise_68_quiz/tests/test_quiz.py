import unittest

from solution import (
    quiz_score,
)


class QuizScoreTests(unittest.TestCase):

    def test_all_answers_correct(
        self,
    ) -> None:
        user_answers: list[str] = ["a", "b"]
        correct_answers: list[str] = ["a", "b"]
        expected_score: int = 2

        actual_score: int = quiz_score(
            user_answers,
            correct_answers,
        )

        self.assertEqual(
            actual_score,
            expected_score,
        )

    def test_no_answers_correct(
        self,
    ) -> None:
        user_answers: list[str] = ["a", "b"]
        correct_answers: list[str] = ["c", "d"]
        expected_score: int = 0

        actual_score: int = quiz_score(
            user_answers,
            correct_answers,
        )

        self.assertEqual(
            actual_score,
            expected_score,
        )


if __name__ == "__main__":
    unittest.main()
