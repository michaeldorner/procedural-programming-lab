import unittest

from solution import (
    count_vowels,
)


class Exercise44BonusTests(unittest.TestCase):

    def test_count_vowels_1(
        self,
    ) -> None:
        value_0 = 'AEIOU'
        expected_result = 5

        actual_result = count_vowels(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
