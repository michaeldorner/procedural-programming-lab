import unittest

from solution import (
    lookup_phone,
)


class PhoneBookLookupTests(unittest.TestCase):

    def test_existing_contact(
        self,
    ) -> None:
        phone_book: dict[str, str] = {"Alice": "123"}
        contact_name: str = "Alice"
        expected_number: str = "123"

        actual_number: str = lookup_phone(
            phone_book,
            contact_name,
        )

        self.assertEqual(
            actual_number,
            expected_number,
        )

    def test_missing_contact_returns_empty_string(
        self,
    ) -> None:
        phone_book: dict[str, str] = {"Alice": "123"}
        contact_name: str = "Bob"
        expected_number: str = ""

        actual_number: str = lookup_phone(
            phone_book,
            contact_name,
        )

        self.assertEqual(
            actual_number,
            expected_number,
        )


if __name__ == "__main__":
    unittest.main()
