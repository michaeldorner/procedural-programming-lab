from datetime import time

def minutes_between(
    start: time,
    end: time,
) -> int:
    start_minutes = start.hour * 60 + start.minute
    end_minutes = end.hour * 60 + end.minute
    if end_minutes < start_minutes:
        end_minutes += 24 * 60
    return end_minutes - start_minutes
