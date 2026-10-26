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


STATUS_TEXT = {
    Status.FAILED: "❌ Failed",
    Status.PASSED: "✅ Passed",
}


ASCII_TEMPLATE = """
═══════════════════════════════════════
 Procedural Programming Progress
═══════════════════════════════════════

{exercise_results}

{progress_bar} {completion}

Completed          {completed}/{total}
""".strip()


MARKDOWN_TEMPLATE = """
# Procedural Programming Progress

| Exercise | Status |
|---|---|
{exercise_results}

## Summary

- Completed: {completed}/{total}
""".strip()


def parse_arguments() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
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
    test_directory: str = "tests",
) -> bool:
    test_cmd: str = f"""
import sys, pathlib, unittest
if pathlib.Path('reference_solution.py').exists():
    import reference_solution
    sys.modules['solution'] = reference_solution
unittest.main(
    module=None,
    argv=['unittest', 'discover', '{test_directory}', '-v'],
)
"""
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

    return result.returncode == 0


def exercise_status(
    exercise: Path,
) -> Status:
    tests_directory: Path = exercise / "tests"
    required_test_file: Path = (
        tests_directory / "required" / "test_required.py"
    )

    if required_test_file.exists():
        required_passed: bool = test_passed(
            exercise,
            "tests/required",
        )
        if not required_passed:
            return Status.FAILED

        bonus_test_file: Path = (
            tests_directory / "bonus" / "test_bonus.py"
        )
        if bonus_test_file.exists():
            bonus_passed: bool = test_passed(
                exercise,
                "tests/bonus",
            )
            if not bonus_passed:
                return Status.FAILED

        return Status.PASSED

    all_passed: bool = test_passed(
        exercise,
        "tests",
    )
    return Status.PASSED if all_passed else Status.FAILED


def collect_results() -> dict[str, Status]:
    results: dict[str, Status] = {}

    exercises: list[Path] = sorted(
        [
            exercise
            for exercise in Path(".").rglob("exercise_*")
            if exercise.is_dir()
        ]
    )

    for exercise in exercises:
        rel_path: str = str(exercise.relative_to(Path(".")))
        results[rel_path] = exercise_status(
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


def progress_bar(
    completion: float,
    width: int = 20,
) -> str:
    filled: int = int(completion * width)
    empty: int = width - filled

    return "█" * filled + "░" * empty


def render_ascii_exercise_results(
    results: dict[str, Status],
) -> str:
    lines: list[str] = []
    width: int = max((len(name) for name in results), default=12)

    for exercise, status in results.items():
        lines.append(
            f"{exercise:<{width}}  {STATUS_TEXT[status]}",
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
    total: int = len(results)

    if total == 0:
        return "No exercises found."

    completed: int = count_completed(results)
    completion: float = completed / total

    return ASCII_TEMPLATE.format(
        exercise_results=render_ascii_exercise_results(
            results,
        ),
        progress_bar=progress_bar(
            completion,
        ),
        completion=f"{completion:.0%}",
        completed=completed,
        total=total,
    )


def render_markdown(
    results: dict[str, Status],
) -> str:
    total: int = len(results)

    if total == 0:
        return "# Procedural Programming Progress\n\nNo exercises found."

    completed: int = count_completed(results)

    return MARKDOWN_TEMPLATE.format(
        exercise_results=render_markdown_exercise_results(
            results,
        ),
        completed=completed,
        total=total,
    )


def main() -> None:
    args: argparse.Namespace = parse_arguments()
    output_format: OutputFormat = OutputFormat(args.format)

    results: dict[str, Status] = collect_results()

    if output_format == OutputFormat.MARKDOWN:
        print(render_markdown(results))
    else:
        print(render_ascii(results))

    # if count_completed(results) < len(results):
    #     sys.exit(1)


if __name__ == "__main__":
    main()
