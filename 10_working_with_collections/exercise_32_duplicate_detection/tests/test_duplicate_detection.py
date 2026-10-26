import unittest

from solution import (
    has_duplicates,
)


class DuplicateDetectionTests(unittest.TestCase):

    def test_list_containing_duplicates(
        self,
    ) -> None:
        numbers: list[int] = [1, 2, 1]

        duplicates_found: bool = has_duplicates(
            numbers,
        )

        self.assertTrue(
            duplicates_found,
        )

    def test_list_with_unique_elements(
        self,
    ) -> None:
        numbers: list[int] = [1, 2, 3]

        duplicates_found: bool = has_duplicates(
            numbers,
        )

        self.assertFalse(
            duplicates_found,
        )


if __name__ == "__main__":
    unittest.main()
