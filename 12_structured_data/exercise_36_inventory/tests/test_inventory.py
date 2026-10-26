import unittest

from solution import (
    update_inventory,
)


class UpdateInventoryTests(unittest.TestCase):

    def test_increment_existing_item(
        self,
    ) -> None:
        inventory: dict[str, int] = {"apple": 5}
        item_name: str = "apple"
        quantity_to_add: int = 3
        expected_inventory: dict[str, int] = {"apple": 8}

        actual_inventory: dict[str, int] = update_inventory(
            inventory,
            item_name,
            quantity_to_add,
        )

        self.assertEqual(
            actual_inventory,
            expected_inventory,
        )

    def test_add_new_item(
        self,
    ) -> None:
        inventory: dict[str, int] = {"apple": 5}
        item_name: str = "banana"
        quantity_to_add: int = 2
        expected_inventory: dict[str, int] = {"apple": 5, "banana": 2}

        actual_inventory: dict[str, int] = update_inventory(
            inventory,
            item_name,
            quantity_to_add,
        )

        self.assertEqual(
            actual_inventory,
            expected_inventory,
        )


if __name__ == "__main__":
    unittest.main()
