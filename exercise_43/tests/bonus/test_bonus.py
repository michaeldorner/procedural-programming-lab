import unittest

from solution import (
    reverse_string,
)


class Exercise43BonusTests(unittest.TestCase):

    def test_reverse_string_1(
        self,
    ) -> None:
        value_0 = ''
        expected_result = ''

        actual_result = reverse_string(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
