from enum import Enum


class GradeLevel(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    PASS = "pass"
    FAIL = "fail"


# Student template
def grade_level(
    score: int,
) -> GradeLevel:
    pass


# Basic solution
def grade_level(
    score: int,
) -> GradeLevel:
    if score >= 90:
        return GradeLevel.EXCELLENT
    if score >= 70:
        return GradeLevel.GOOD
    return GradeLevel.FAIL


# Excellent solution for bonus tests
def grade_level(
    score: int,
) -> GradeLevel:
    if score >= 90:
        return GradeLevel.EXCELLENT
    if score >= 70:
        return GradeLevel.GOOD
    if score >= 60:
        return GradeLevel.PASS
    return GradeLevel.FAIL
