import unittest

from solution import (
    common_elements,
)


class CommonElementsTests(unittest.TestCase):

    def test_overlapping_lists(
        self,
    ) -> None:
        first_list: list[int] = [1, 2, 3]
        second_list: list[int] = [2, 3, 4]
        expected_common: set[int] = {2, 3}

        actual_common: set[int] = common_elements(
            first_list,
            second_list,
        )

        self.assertEqual(
            actual_common,
            expected_common,
        )

    def test_disjoint_lists(
        self,
    ) -> None:
        first_list: list[int] = [1]
        second_list: list[int] = [2]
        expected_common: set[int] = set()

        actual_common: set[int] = common_elements(
            first_list,
            second_list,
        )

        self.assertEqual(
            actual_common,
            expected_common,
        )


if __name__ == "__main__":
    unittest.main()
