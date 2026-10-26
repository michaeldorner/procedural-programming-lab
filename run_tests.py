import subprocess
import sys
from pathlib import Path

failed: int = 0
exercises: list[Path] = sorted(
    [
        exercise
        for exercise in Path(".").rglob("exercise_*")
        if exercise.is_dir()
    ]
)

test_cmd: str = """
import sys, pathlib, unittest
if pathlib.Path('reference_solution.py').exists():
    import reference_solution
    sys.modules['solution'] = reference_solution
unittest.main(
    module=None,
    argv=['unittest', 'discover', 'tests', '-v'],
)
"""

for exercise in exercises:
    result: subprocess.CompletedProcess[bytes] = subprocess.run(
        [
            sys.executable,
            "-c",
            test_cmd,
        ],
        cwd=exercise,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    rel_path: Path = exercise.relative_to(Path("."))
    if result.returncode == 0:
        print(f"✅ {rel_path}")
    else:
        print(f"❌ {rel_path}")
        failed = 1
sys.exit(failed)

