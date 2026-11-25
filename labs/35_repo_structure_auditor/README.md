# Lab 35: Repo Structure Auditor

**Topics:** Filesystem paths (`pathlib`), recursive globbing, file I/O, exception handling  
**Lectures:** 07 (Validation & Exceptions), 09 (Built-in Collections), 15 (File Processing)

Audit a labs directory tree to list Python modules, detect folders missing a README, and count non-empty lines.

## Requirements

- Implement `list_python_files` to return sorted paths of all `.py` files recursively under a root directory (empty list if root is missing).
- Implement `find_labs_missing_readme` to return sorted names of immediate subdirectories lacking `README.md`.
- Implement `count_non_empty_lines` to count lines containing non-whitespace characters, returning no value if the file cannot be read.

## Worked Examples

- A subdirectory without `README.md` appears in `find_labs_missing_readme`.

## Implementation Hints

- See [`pathlib.Path.rglob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob) and [`pathlib.Path.iterdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir).

## Run & Test

```bash
python repo_structure_auditor.py
python -m unittest
```
