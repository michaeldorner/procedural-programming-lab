import unittest

from solution import (
    library_search,
)


class LibrarySearchTests(unittest.TestCase):

    def test_existing_book_found(
        self,
    ) -> None:
        book_catalog: list[dict[str, str]] = [{"title": "Dune", "author": "Frank Herbert"}]
        query_title: str = "Dune"
        expected_book: dict[str, str] = {"title": "Dune", "author": "Frank Herbert"}

        actual_book: dict[str, str] | None = library_search(
            book_catalog,
            query_title,
        )

        self.assertEqual(
            actual_book,
            expected_book,
        )

    def test_nonexistent_book_returns_none(
        self,
    ) -> None:
        book_catalog: list[dict[str, str]] = [{"title": "Dune", "author": "Frank Herbert"}]
        query_title: str = "Foundation"

        actual_book: dict[str, str] | None = library_search(
            book_catalog,
            query_title,
        )

        self.assertIsNone(
            actual_book,
        )


if __name__ == "__main__":
    unittest.main()
