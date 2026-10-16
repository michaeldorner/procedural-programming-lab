import unittest

from solution import (
    count_vowels,
)


class Exercise44RequiredTests(unittest.TestCase):

    def test_count_vowels_1(
        self,
    ) -> None:
        value_0 = 'hello'
        expected_result = 2

        actual_result = count_vowels(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
