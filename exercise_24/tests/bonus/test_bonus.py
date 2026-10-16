import unittest

from solution import (
    remove_duplicates,
)


class Exercise24BonusTests(unittest.TestCase):

    def test_remove_duplicates_1(
        self,
    ) -> None:
        value_0 = []
        expected_result = []

        actual_result = remove_duplicates(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
