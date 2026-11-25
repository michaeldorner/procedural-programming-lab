"""Unit tests for slug_normalizer."""

import unittest

from .slug_normalizer import normalize_slug


class TestSlugNormalizer(unittest.TestCase):
    """Tests for normalize_slug."""

    def test_slugification(self) -> None:
        self.assertEqual(normalize_slug("  Hello, World!  2026 "), "hello-world-2026")
        self.assertEqual(normalize_slug("one__two---three"), "one-two-three")
        self.assertEqual(normalize_slug("___!!!"), "")
