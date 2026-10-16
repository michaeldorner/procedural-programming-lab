import unittest

from solution import is_valid_isbn10


class Exercise05RequiredTests(unittest.TestCase):

    def test_valid_isbn10(
        self,
    ) -> None:
        isbn: str = "0306406152"

        actual_result: bool = is_valid_isbn10(
            isbn,
        )

        self.assertTrue(
            actual_result,
        )

    def test_invalid_isbn10_check_digit(
        self,
    ) -> None:
        isbn: str = "0306406153"

        actual_result: bool = is_valid_isbn10(
            isbn,
        )

        self.assertFalse(
            actual_result,
        )

    def test_invalid_isbn10_length(
        self,
    ) -> None:
        isbn: str = "030640615"

        actual_result: bool = is_valid_isbn10(
            isbn,
        )

        self.assertFalse(
            actual_result,
        )


if __name__ == "__main__":
    unittest.main()
