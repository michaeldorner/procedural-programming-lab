import unittest

from solution import (
    has_duplicates,
)


class Exercise32RequiredTests(unittest.TestCase):

    def test_has_duplicates_1(
        self,
    ) -> None:
        value_0 = [1, 2, 1]
        expected_result = True

        actual_result = has_duplicates(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_has_duplicates_2(
        self,
    ) -> None:
        value_0 = [1, 2, 3]
        expected_result = False

        actual_result = has_duplicates(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
