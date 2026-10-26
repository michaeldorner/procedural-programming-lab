from enum import Enum


class GradeLevel(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    PASS = "pass"
    FAIL = "fail"

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
