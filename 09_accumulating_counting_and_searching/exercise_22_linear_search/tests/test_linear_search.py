import unittest

from solution import (
    linear_search,
)


class LinearSearchTests(unittest.TestCase):

    def test_element_found_in_middle(
        self,
    ) -> None:
        elements: list[int] = [4, 5, 6]
        target: int = 5
        expected_index: int = 1

        actual_index: int = linear_search(
            elements,
            target,
        )

        self.assertEqual(
            actual_index,
            expected_index,
        )

    def test_returns_first_matching_index(
        self,
    ) -> None:
        elements: list[int] = [1, 1, 2]
        target: int = 1
        expected_index: int = 0

        actual_index: int = linear_search(
            elements,
            target,
        )

        self.assertEqual(
            actual_index,
            expected_index,
        )


if __name__ == "__main__":
    unittest.main()
