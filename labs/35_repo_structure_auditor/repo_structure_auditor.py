"""Lab 35: Repo Structure Auditor."""

from pathlib import Path


def list_python_files(root: Path) -> list[Path]:
    """Return sorted Paths of all .py files recursively under root."""
    raise NotImplementedError


def find_labs_missing_readme(labs_dir: Path) -> list[str]:
    """Return sorted names of immediate subdirectories of labs_dir missing README.md."""
    raise NotImplementedError


def count_non_empty_lines(file_path: Path) -> int | None:
    """Return count of non-empty lines in file_path, or None on OSError."""
    raise NotImplementedError


if __name__ == "__main__":
    print("Missing READMEs:", find_labs_missing_readme(Path("..")))
