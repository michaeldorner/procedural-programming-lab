"""Lab 30: Course Prerequisite Checker."""


def find_missing_prerequisites(
    course: str,
    completed: set[str],
    prereqs_by_course: dict[str, set[str]],
) -> set[str]:
    """Return prerequisites required for course that are not in completed."""
    raise NotImplementedError


def can_enroll(
    course: str,
    completed: set[str],
    prereqs_by_course: dict[str, set[str]],
) -> bool:
    """Return True if all prerequisites for course are in completed."""
    raise NotImplementedError


def find_unlocked_courses(
    completed: set[str],
    prereqs_by_course: dict[str, set[str]],
) -> set[str]:
    """Return courses not in completed whose prerequisites are all satisfied."""
    raise NotImplementedError


if __name__ == "__main__":
    prereqs = {"CS101": set(), "CS102": {"CS101"}, "CS201": {"CS102"}}
    print("unlocked:", find_unlocked_courses({"CS101"}, prereqs))
