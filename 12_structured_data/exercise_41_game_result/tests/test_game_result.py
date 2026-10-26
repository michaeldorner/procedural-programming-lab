import unittest

from solution import (
    GameResult,
    points_for_result,
)


class GameResultPointsTests(unittest.TestCase):

    def test_win_awards_three_points(
        self,
    ) -> None:
        outcome: GameResult = GameResult.WIN
        expected_points: int = 3

        actual_points: int = points_for_result(
            outcome,
        )

        self.assertEqual(
            actual_points,
            expected_points,
        )

    def test_draw_awards_one_point(
        self,
    ) -> None:
        outcome: GameResult = GameResult.DRAW
        expected_points: int = 1

        actual_points: int = points_for_result(
            outcome,
        )

        self.assertEqual(
            actual_points,
            expected_points,
        )

    def test_loss_awards_zero_points(
        self,
    ) -> None:
        outcome: GameResult = GameResult.LOSS
        expected_points: int = 0

        actual_points: int = points_for_result(
            outcome,
        )

        self.assertEqual(
            actual_points,
            expected_points,
        )


if __name__ == "__main__":
    unittest.main()
