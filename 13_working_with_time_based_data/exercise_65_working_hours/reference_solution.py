from datetime import time

def is_working_hour(
    value: time,
) -> bool:
    return time(9, 0) <= value < time(17, 0)
