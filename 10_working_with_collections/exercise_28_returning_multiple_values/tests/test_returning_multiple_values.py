import unittest

from solution import (
    split_name,
)


class SplitNameTests(unittest.TestCase):

    def test_first_and_last_name_ada(
        self,
    ) -> None:
        full_name: str = "Ada Lovelace"
        expected_parts: tuple[str, str] = ("Ada", "Lovelace")

        actual_parts: tuple[str, str] = split_name(
            full_name,
        )

        self.assertEqual(
            actual_parts,
            expected_parts,
        )

    def test_first_and_last_name_alan(
        self,
    ) -> None:
        full_name: str = "Alan Turing"
        expected_parts: tuple[str, str] = ("Alan", "Turing")

        actual_parts: tuple[str, str] = split_name(
            full_name,
        )

        self.assertEqual(
            actual_parts,
            expected_parts,
        )


if __name__ == "__main__":
    unittest.main()
