import unittest

from solution import (
    update_inventory,
)


class Exercise36RequiredTests(unittest.TestCase):

    def test_update_inventory_1(
        self,
    ) -> None:
        value_0 = {'apple': 2}
        value_1 = 'apple'
        value_2 = 3
        expected_result = {'apple': 5}

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
