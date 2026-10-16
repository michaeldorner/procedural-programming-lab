from datetime import time


# Student template
def minutes_between(
    start: time,
    end: time,
) -> int:
    pass


# Basic solution
def minutes_between(
    start: time,
    end: time,
) -> int:
    start_minutes = start.hour * 60 + start.minute
    end_minutes = end.hour * 60 + end.minute
    return end_minutes - start_minutes


# Excellent solution for bonus tests
def minutes_between(
    start: time,
    end: time,
) -> int:
    start_minutes = start.hour * 60 + start.minute
    end_minutes = end.hour * 60 + end.minute
    if end_minutes < start_minutes:
        end_minutes += 24 * 60
    return end_minutes - start_minutes
