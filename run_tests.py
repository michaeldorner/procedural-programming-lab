from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
import subprocess


class TestCategory(StrEnum):
    REQUIRED = "required"
    BONUS = "bonus"


@dataclass
class Progress:
    completed: int = 0
    distinction: int = 0


REPORT_TEMPLATE = """
═══════════════════════════════════════
 Procedural Programming Progress
═══════════════════════════════════════

{results}

{bar} {completion}

Completed          {completed}/{total}
With distinction   {distinction}/{total}
""".strip()


def test_suite_passed(
    exercise: Path,
    category: TestCategory,
) -> bool:
    result = subprocess.run(
        [
            "python",
            "-m",
            "unittest",
            "discover",
            f"tests/{category.value}",
        ],
        cwd=exercise,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return result.returncode == 0


def progress_bar(
    progress: float,
    width: int = 20,
) -> str:
    filled = int(progress * width)

    return (
        "█" * filled
        + "░" * (width - filled)
    )


def print_progress(
    results: list[str],
    progress: Progress,
) -> None:
    total = len(results)

    if total == 0:
        print("No exercises found.")
        return

    completion = progress.completed / total

    report = REPORT_TEMPLATE.format(
        results="\n".join(results),
        bar=progress_bar(completion),
        completion=f"{completion:.0%}",
        completed=progress.completed,
        distinction=progress.distinction,
        total=total,
    )

    print(report)


def main() -> None:
    progress = Progress()

    results: list[str] = []

    for exercise in sorted(
        Path(".").glob("exercise_*")
    ):
        if not test_suite_passed(
            exercise,
            TestCategory.REQUIRED,
        ):
            results.append(
                f"❌ {exercise.name}"
            )
            continue

        progress.completed += 1

        bonus_directory = (
            exercise
            / "tests"
            / TestCategory.BONUS.value
        )

        if (
            bonus_directory.exists()
            and test_suite_passed(
                exercise,
                TestCategory.BONUS,
            )
        ):
            progress.distinction += 1

            results.append(
                f"🌟 {exercise.name}"
            )
        else:
            results.append(
                f"✅ {exercise.name}"
            )

    print_progress(
        results,
        progress,
    )


if __name__ == "__main__":
    main()
