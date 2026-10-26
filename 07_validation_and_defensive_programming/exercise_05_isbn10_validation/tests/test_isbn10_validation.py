import unittest

from solution import is_valid_isbn10


class ValidISBN10Tests(unittest.TestCase):

    def test_unformatted_standard_isbn(
        self,
    ) -> None:
        isbn: str = "0306406152"

        validity: bool = is_valid_isbn10(
            isbn,
        )

        self.assertTrue(
            validity,
        )

    def test_isbn_with_hyphens(
        self,
    ) -> None:
        isbn: str = "0-306-40615-2"

        validity: bool = is_valid_isbn10(
            isbn,
        )

        self.assertTrue(
            validity,
        )

    def test_isbn_with_spaces(
        self,
    ) -> None:
        isbn: str = "0 306 40615 2"

        validity: bool = is_valid_isbn10(
            isbn,
        )

        self.assertTrue(
            validity,
        )

    def test_isbn_with_uppercase_x_check_digit(
        self,
    ) -> None:
        isbn: str = "080442957X"

        validity: bool = is_valid_isbn10(
            isbn,
        )

        self.assertTrue(
            validity,
        )

    def test_isbn_with_lowercase_x_check_digit(
        self,
    ) -> None:
        isbn: str = "080442957x"

        validity: bool = is_valid_isbn10(
            isbn,
        )

        self.assertTrue(
            validity,
        )


class InvalidISBN10Tests(unittest.TestCase):

    def test_invalid_check_digit(
        self,
    ) -> None:
        isbn: str = "0306406153"

        validity: bool = is_valid_isbn10(
            isbn,
        )

        self.assertFalse(
            validity,
        )

    def test_too_short_isbn(
        self,
    ) -> None:
        isbn: str = "030640615"

        validity: bool = is_valid_isbn10(
            isbn,
        )

        self.assertFalse(
            validity,
        )

    def test_invalid_x_check_digit(
        self,
    ) -> None:
        isbn: str = "080442958X"

        validity: bool = is_valid_isbn10(
            isbn,
        )

        self.assertFalse(
            validity,
        )


if __name__ == "__main__":
    unittest.main()
