"""Unit tests for slug_normalizer."""

import unittest

from slug_normalizer import to_slug


class TestSlugNormalizer(unittest.TestCase):
    """Tests for to_slug."""

    def test_slugification(self) -> None:
        self.assertEqual(to_slug("  Hello, World!  2026 "), "hello-world-2026")
        self.assertEqual(to_slug("one__two---three"), "one-two-three")
        self.assertEqual(to_slug("___!!!"), "")
