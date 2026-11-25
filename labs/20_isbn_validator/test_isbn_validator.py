"""Unit tests for isbn_validator."""

import unittest

from isbn_validator import is_valid_isbn10, is_valid_isbn13


class TestIsbnValidator(unittest.TestCase):
    """Tests for ISBN-10 and ISBN-13 validation."""

    def test_isbn10(self) -> None:
        self.assertIs(is_valid_isbn10("0-306-40615-2"), True)
        self.assertIs(is_valid_isbn10("043942089X"), True)
        self.assertIs(is_valid_isbn10("0-306-40615-3"), False)
        self.assertIs(is_valid_isbn10("X306406152"), False)

    def test_isbn13(self) -> None:
        self.assertIs(is_valid_isbn13("978-0-306-40615-7"), True)
        self.assertIs(is_valid_isbn13("978-0-306-40615-8"), False)
        self.assertIs(is_valid_isbn13("12345"), False)
