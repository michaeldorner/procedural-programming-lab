import unittest

from solution import (
    group_by_category,
)


class Exercise55BonusTests(unittest.TestCase):

    def test_group_by_category_1(
        self,
    ) -> None:
        value_0 = []
        expected_result = {}

        actual_result = group_by_category(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
