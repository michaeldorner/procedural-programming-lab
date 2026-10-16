import unittest

from solution import (
    unique_values,
)


class Exercise29BonusTests(unittest.TestCase):

    def test_unique_values_1(
        self,
    ) -> None:
        value_0 = []
        expected_result = set()

        actual_result = unique_values(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
