"""Unit tests for zen."""

from contextlib import redirect_stdout
import importlib
import io
import sys
import unittest


class TestZen(unittest.TestCase):
    """Verify that importing zen prints The Zen of Python."""

    def test_zen_output_on_import(self) -> None:
        sys.modules.pop("this", None)
        sys.modules.pop("zen", None)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            importlib.import_module("zen")
        output = buffer.getvalue()
        self.assertIn("The Zen of Python, by Tim Peters", output)
        self.assertIn("Simple is better than complex.", output)
