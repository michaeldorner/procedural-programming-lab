"""Unit tests for run_length_encoding."""

import unittest

from .run_length_encoding import decode_rle, encode_rle


class TestRunLengthEncoding(unittest.TestCase):
    """Tests for encode_rle and decode_rle."""

    def test_round_trip(self) -> None:
        self.assertEqual(encode_rle(""), "")
        self.assertEqual(decode_rle(""), "")
        self.assertEqual(encode_rle("AAABBC"), "3A2B1C")
        self.assertEqual(decode_rle("12A1B"), "AAAAAAAAAAAA" + "B")

    def test_invalid_inputs_return_none(self) -> None:
        self.assertIsNone(encode_rle("A2B"))
        self.assertIsNone(decode_rle("ABC"))
        self.assertIsNone(decode_rle("0A"))
        self.assertIsNone(decode_rle("3A2"))
