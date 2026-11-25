"""Unit tests for run_length_encoding."""

import unittest

from run_length_encoding import rle_decode, rle_encode


class TestRunLengthEncoding(unittest.TestCase):
    """Tests for rle_encode and rle_decode."""

    def test_round_trip(self) -> None:
        self.assertEqual(rle_encode(""), "")
        self.assertEqual(rle_decode(""), "")
        self.assertEqual(rle_encode("AAABBC"), "3A2B1C")
        self.assertEqual(rle_decode("12A1B"), "AAAAAAAAAAAA" + "B")

    def test_invalid_inputs_return_none(self) -> None:
        self.assertIsNone(rle_encode("A2B"))
        self.assertIsNone(rle_decode("ABC"))
        self.assertIsNone(rle_decode("0A"))
        self.assertIsNone(rle_decode("3A2"))
