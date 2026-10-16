import unittest

from solution import (
    quiz_score,
)


class Exercise68RequiredTests(unittest.TestCase):

    def test_quiz_score_1(
        self,
    ) -> None:
        value_0 = ['a', 'b', 'c']
        value_1 = ['a', 'x', 'c']
        expected_result = 2

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
