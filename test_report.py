from enum import StrEnum
from pathlib import Path
import argparse
import subprocess
import sys


class OutputFormat(StrEnum):
    ASCII = "ascii"
    MARKDOWN = "markdown"


class Status(StrEnum):
    FAILED = "failed"
    PASSED = "passed"
    DISTINCTION = "distinction"


STATUS_TEXT = {
    Status.FAILED: "❌ Failed",
    Status.PASSED: "✅ Passed",
    Status.DISTINCTION: "🌟 Passed with distinction",
}


ASCII_TEMPLATE = """
═══════════════════════════════════════
 Procedural Programming Progress
═══════════════════════════════════════

{exercise_results}

{progress_bar} {completion}

Completed          {completed}/{total}
With distinction   {distinction}/{total}
""".strip()


MARKDOWN_TEMPLATE = """
# Procedural Programming Progress

| Exercise | Status |
|---|---|
{exercise_results}

## Summary

- Completed: {completed}/{total}
- With distinction: {distinction}/{total}
""".strip()


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an exercise progress report.",
    )

    parser.add_argument(
        "--format",
        choices=[
            OutputFormat.ASCII.value,
            OutputFormat.MARKDOWN.value,
        ],
        default=OutputFormat.ASCII.value,
        help="Output format.",
    )

    return parser.parse_args()


def test_passed(
    exercise: Path,
    test_directory: str,
) -> bool:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            test_directory,
            "-v",
        ],
        cwd=exercise,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return result.returncode == 0


def exercise_status(
    exercise: Path,
) -> Status:
    required_passed = test_passed(
        exercise,
        "tests/required",
    )

    if not required_passed:
        return Status.FAILED

    bonus_directory = exercise / "tests" / "bonus"

    if bonus_directory.exists():
        bonus_passed = test_passed(
            exercise,
            "tests/bonus",
        )

        if bonus_passed:
            return Status.DISTINCTION

    return Status.PASSED


def collect_results() -> dict[str, Status]:
    results: dict[str, Status] = {}

    for exercise in sorted(Path(".").glob("exercise_*")):
        if exercise.is_dir():
            results[exercise.name] = exercise_status(
                exercise,
            )

    return results


def count_completed(
    results: dict[str, Status],
) -> int:
    return sum(
        status != Status.FAILED
        for status in results.values()
    )


def count_distinction(
    results: dict[str, Status],
) -> int:
    return sum(
        status == Status.DISTINCTION
        for status in results.values()
    )


def progress_bar(
    completion: float,
    width: int = 20,
) -> str:
    filled = int(completion * width)
    empty = width - filled

    return "█" * filled + "░" * empty


def render_ascii_exercise_results(
    results: dict[str, Status],
) -> str:
    lines: list[str] = []

    for exercise, status in results.items():
        lines.append(
            f"{exercise:<12} {STATUS_TEXT[status]}",
        )

    return "\n".join(lines)


def render_markdown_exercise_results(
    results: dict[str, Status],
) -> str:
    lines: list[str] = []

    for exercise, status in results.items():
        lines.append(
            f"| {exercise} | {STATUS_TEXT[status]} |",
        )

    return "\n".join(lines)


def render_ascii(
    results: dict[str, Status],
) -> str:
    total = len(results)

    if total == 0:
        return "No exercises found."

    completed = count_completed(results)
    distinction = count_distinction(results)
    completion = completed / total

    return ASCII_TEMPLATE.format(
        exercise_results=render_ascii_exercise_results(
            results,
        ),
        progress_bar=progress_bar(
            completion,
        ),
        completion=f"{completion:.0%}",
        completed=completed,
        distinction=distinction,
        total=total,
    )


def render_markdown(
    results: dict[str, Status],
) -> str:
    total = len(results)

    if total == 0:
        return "# Procedural Programming Progress\n\nNo exercises found."

    completed = count_completed(results)
    distinction = count_distinction(results)

    return MARKDOWN_TEMPLATE.format(
        exercise_results=render_markdown_exercise_results(
            results,
        ),
        completed=completed,
        distinction=distinction,
        total=total,
    )


def main() -> None:
    args = parse_arguments()
    output_format = OutputFormat(args.format)

    results = collect_results()

    if output_format == OutputFormat.MARKDOWN:
        print(render_markdown(results))
    else:
        print(render_ascii(results))

    # if count_completed(results) < len(results):
    #     sys.exit(1)


if __name__ == "__main__":
    main()
