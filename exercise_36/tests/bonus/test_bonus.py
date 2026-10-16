import unittest

from solution import (
    update_inventory,
)


class Exercise36BonusTests(unittest.TestCase):

    def test_update_inventory_1(
        self,
    ) -> None:
        value_0 = {}
        value_1 = 'pear'
        value_2 = 4
        expected_result = {'pear': 4}

        actual_result = update_inventory(
            value_0,
            value_1,
            value_2,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
