import unittest

from solution import (
    guess_feedback,
)


class Exercise67BonusTests(unittest.TestCase):

    def test_guess_feedback_1(
        self,
    ) -> None:
        value_0 = -1
        value_1 = -1
        expected_result = 'correct'

        actual_result = guess_feedback(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
