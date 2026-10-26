import unittest

from solution import (
    group_by_category,
)


class GroupByCategoryTests(unittest.TestCase):

    def test_categorized_items(
        self,
    ) -> None:
        items: list[dict[str, str]] = [
            {"category": "fruit", "name": "apple"},
            {"category": "fruit", "name": "banana"},
            {"category": "dairy", "name": "milk"},
        ]
        expected_groups: dict[str, list[str]] = {
            "fruit": ["apple", "banana"],
            "dairy": ["milk"],
        }

        actual_groups: dict[str, list[str]] = group_by_category(
            items,
        )

        self.assertEqual(
            actual_groups,
            expected_groups,
        )

    def test_empty_item_list(
        self,
    ) -> None:
        items: list[dict[str, str]] = []
        expected_groups: dict[str, list[str]] = {}

        actual_groups: dict[str, list[str]] = group_by_category(
            items,
        )

        self.assertEqual(
            actual_groups,
            expected_groups,
        )


if __name__ == "__main__":
    unittest.main()
