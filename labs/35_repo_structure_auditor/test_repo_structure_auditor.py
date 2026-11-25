"""Unit tests for repo_structure_auditor."""

from pathlib import Path
import tempfile
import unittest

from repo_structure_auditor import (
    count_non_empty_lines,
    find_labs_missing_readme,
    list_python_files,
)


class TestRepoStructureAuditor(unittest.TestCase):
    """Tests for repository structure auditing helpers."""

    def test_auditor_helpers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            lab_a = root / "01_a"
            lab_b = root / "02_b"
            lab_a.mkdir()
            lab_b.mkdir()
            (lab_a / "README.md").write_text("# A\n", encoding="utf-8")
            py_file = lab_a / "mod.py"
            py_file.write_text("x = 1\n\n   \ny = 2\n", encoding="utf-8")

            self.assertEqual(list_python_files(root), [py_file])
            self.assertEqual(find_labs_missing_readme(root), ["02_b"])
            self.assertEqual(count_non_empty_lines(py_file), 2)
            self.assertIsNone(count_non_empty_lines(root / "missing.py"))
