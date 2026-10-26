import unittest

from solution import (
    guess_feedback,
)


class GuessFeedbackTests(unittest.TestCase):

    def test_guess_lower_than_secret(
        self,
    ) -> None:
        secret_number: int = 10
        player_guess: int = 5
        expected_feedback: str = "low"

        actual_feedback: str = guess_feedback(
            secret_number,
            player_guess,
        )

        self.assertEqual(
            actual_feedback,
            expected_feedback,
        )

    def test_guess_higher_than_secret(
        self,
    ) -> None:
        secret_number: int = 10
        player_guess: int = 15
        expected_feedback: str = "high"

        actual_feedback: str = guess_feedback(
            secret_number,
            player_guess,
        )

        self.assertEqual(
            actual_feedback,
            expected_feedback,
        )

    def test_guess_matches_secret(
        self,
    ) -> None:
        secret_number: int = 10
        player_guess: int = 10
        expected_feedback: str = "correct"

        actual_feedback: str = guess_feedback(
            secret_number,
            player_guess,
        )

        self.assertEqual(
            actual_feedback,
            expected_feedback,
        )


if __name__ == "__main__":
    unittest.main()
