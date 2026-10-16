import unittest

from solution import (
    guess_feedback,
)


class Exercise67RequiredTests(unittest.TestCase):

    def test_guess_feedback_1(
        self,
    ) -> None:
        value_0 = 10
        value_1 = 5
        expected_result = 'low'

        actual_result = guess_feedback(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_guess_feedback_2(
        self,
    ) -> None:
        value_0 = 10
        value_1 = 15
        expected_result = 'high'

        actual_result = guess_feedback(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_guess_feedback_3(
        self,
    ) -> None:
        value_0 = 10
        value_1 = 10
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
