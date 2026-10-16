import unittest

from solution import (
    most_frequent_word,
)


class Exercise38BonusTests(unittest.TestCase):

    def test_most_frequent_word_1(
        self,
    ) -> None:
        value_0 = ['x']
        expected_result = 'x'

        actual_result = most_frequent_word(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
