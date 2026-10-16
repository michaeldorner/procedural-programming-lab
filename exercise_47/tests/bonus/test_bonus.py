import unittest

from solution import (
    longest_word,
)


class Exercise47BonusTests(unittest.TestCase):

    def test_longest_word_1(
        self,
    ) -> None:
        value_0 = ''
        expected_result = ''

        actual_result = longest_word(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
