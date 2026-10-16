import unittest

from solution import (
    word_count,
)


class Exercise46BonusTests(unittest.TestCase):

    def test_word_count_1(
        self,
    ) -> None:
        value_0 = '  many   spaces  '
        expected_result = 2

        actual_result = word_count(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
