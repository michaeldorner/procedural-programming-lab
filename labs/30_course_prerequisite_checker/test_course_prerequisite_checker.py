"""Unit tests for course_prerequisite_checker."""

import unittest

from .course_prerequisite_checker import (
    can_enroll,
    find_missing_prerequisites,
    find_unlocked_courses,
)


class TestCoursePrerequisiteChecker(unittest.TestCase):
    """Tests for prerequisite and enrollment queries."""

    def test_prerequisite_queries(self) -> None:
        prereqs = {"CS101": set(), "CS102": {"CS101"}, "CS201": {"CS102", "MATH101"}}
        self.assertEqual(find_missing_prerequisites("CS201", {"CS101"}, prereqs), {"CS102", "MATH101"})
        self.assertIs(can_enroll("CS102", {"CS101"}, prereqs), True)
        self.assertIs(can_enroll("CS999", set(), prereqs), True)
        self.assertEqual(find_unlocked_courses({"CS101"}, prereqs), {"CS102"})
