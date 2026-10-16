import unittest

from solution import (
    quiz_score,
)


class Exercise68BonusTests(unittest.TestCase):

    def test_quiz_score_1(
        self,
    ) -> None:
        value_0 = []
        value_1 = []
        expected_result = 0

        actual_result = quiz_score(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
