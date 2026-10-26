import unittest

from solution import (
    contact_search,
)


class ContactSearchTests(unittest.TestCase):

    def test_existing_contact_found(
        self,
    ) -> None:
        contacts: list[dict[str, str]] = [{"name": "Alice", "phone": "123"}]
        query_name: str = "Alice"
        expected_contact: dict[str, str] = {"name": "Alice", "phone": "123"}

        actual_contact: dict[str, str] | None = contact_search(
            contacts,
            query_name,
        )

        self.assertEqual(
            actual_contact,
            expected_contact,
        )

    def test_nonexistent_contact_returns_none(
        self,
    ) -> None:
        contacts: list[dict[str, str]] = [{"name": "Alice", "phone": "123"}]
        query_name: str = "Bob"

        actual_contact: dict[str, str] | None = contact_search(
            contacts,
            query_name,
        )

        self.assertIsNone(
            actual_contact,
        )


if __name__ == "__main__":
    unittest.main()
