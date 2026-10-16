from datetime import time


# Student template
def is_working_hour(
    value: time,
) -> bool:
    pass


# Basic solution
def is_working_hour(
    value: time,
) -> bool:
    return time(9, 0) <= value < time(17, 0)


# Excellent solution for bonus tests
def is_working_hour(
    value: time,
) -> bool:
    return time(9, 0) <= value < time(17, 0)
