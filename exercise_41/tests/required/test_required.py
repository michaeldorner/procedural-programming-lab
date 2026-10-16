import unittest

from solution import (
    GameResult,
    points_for_result,
)


class Exercise41RequiredTests(unittest.TestCase):

    def test_points_for_result_1(
        self,
    ) -> None:
        value_0 = GameResult.WIN
        expected_result = 3

        actual_result = points_for_result(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_points_for_result_2(
        self,
    ) -> None:
        value_0 = GameResult.DRAW
        expected_result = 1

        actual_result = points_for_result(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
