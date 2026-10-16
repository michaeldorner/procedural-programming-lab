import unittest

from solution import (
    word_frequencies,
)


class Exercise34BonusTests(unittest.TestCase):

    def test_word_frequencies_1(
        self,
    ) -> None:
        value_0 = []
        expected_result = {}

        actual_result = word_frequencies(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
