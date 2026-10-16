import unittest

from solution import (
    GameResult,
    points_for_result,
)


class Exercise41BonusTests(unittest.TestCase):

    def test_points_for_result_1(
        self,
    ) -> None:
        value_0 = GameResult.LOSS
        expected_result = 0

        actual_result = points_for_result(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
