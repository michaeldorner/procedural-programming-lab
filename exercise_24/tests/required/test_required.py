import unittest

from solution import (
    remove_duplicates,
)


class Exercise24RequiredTests(unittest.TestCase):

    def test_remove_duplicates_1(
        self,
    ) -> None:
        value_0 = [1, 2, 1, 3, 2]
        expected_result = [1, 2, 3]

        actual_result = remove_duplicates(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
