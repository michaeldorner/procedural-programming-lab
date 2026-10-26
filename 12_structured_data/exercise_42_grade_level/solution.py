from enum import Enum


class GradeLevel(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    PASS = "pass"
    FAIL = "fail"

def grade_level(
    score: int,
) -> GradeLevel:
    pass
