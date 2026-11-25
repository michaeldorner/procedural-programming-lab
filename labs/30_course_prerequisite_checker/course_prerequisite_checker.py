"""Lab 30: Course Prerequisite Checker."""


def missing_prerequisites(
    course: str,
    completed: set[str],
    prereqs_by_course: dict[str, set[str]],
) -> set[str]:
    """Return prerequisites required for course that are not in completed."""
    required: set[str] = prereqs_by_course.get(course, set())
    return required - completed


def can_enroll(
    course: str,
    completed: set[str],
    prereqs_by_course: dict[str, set[str]],
) -> bool:
    """Return True if all prerequisites for course are in completed."""
    return not missing_prerequisites(course, completed, prereqs_by_course)


def unlocked_courses(
    completed: set[str],
    prereqs_by_course: dict[str, set[str]],
) -> set[str]:
    """Return courses not in completed whose prerequisites are all satisfied."""
    return {
        course
        for course in prereqs_by_course
        if course not in completed and can_enroll(course, completed, prereqs_by_course)
    }


if __name__ == "__main__":
    prereqs = {"CS101": set(), "CS102": {"CS101"}, "CS201": {"CS102"}}
    print("unlocked:", unlocked_courses({"CS101"}, prereqs))
