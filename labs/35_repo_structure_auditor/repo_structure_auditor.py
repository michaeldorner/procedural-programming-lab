"""Lab 35: Repo Structure Auditor."""

from pathlib import Path


def list_python_files(root: Path) -> list[Path]:
    """Return sorted Paths of all .py files recursively under root."""
    if not root.is_dir():
        return []
    return sorted(p for p in root.rglob("*.py") if p.is_file())


def find_labs_missing_readme(labs_dir: Path) -> list[str]:
    """Return sorted names of immediate subdirectories of labs_dir missing README.md."""
    if not labs_dir.is_dir():
        return []
    missing: list[str] = []
    for entry in labs_dir.iterdir():
        if entry.is_dir() and not (entry / "README.md").is_file():
            missing.append(entry.name)
    return sorted(missing)


def count_non_empty_lines(file_path: Path) -> int | None:
    """Return count of non-empty lines in file_path, or None on OSError."""
    try:
        with open(file_path, encoding="utf-8") as handle:
            return sum(1 for line in handle if line.strip())
    except OSError:
        return None


if __name__ == "__main__":
    print("Missing READMEs:", find_labs_missing_readme(Path("..")))
