from pathlib import Path
import subprocess
import sys

failed = 0
for exercise in sorted(Path(".").glob("exercise_*")):
    if not exercise.is_dir():
        continue
    result = subprocess.run([sys.executable, "-m", "unittest", "discover", "tests", "-v"], cwd=exercise, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"✅ {exercise.name}")
    else:
        print(f"❌ {exercise.name}")
        failed = 1
sys.exit(failed)
