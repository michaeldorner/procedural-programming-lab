# Student template
def split_name(
    full_name: str,
) -> tuple[str, str]:
    pass


# Basic solution
def split_name(
    full_name: str,
) -> tuple[str, str]:
    first_name, last_name = full_name.split()
    return first_name, last_name


# Excellent solution for bonus tests
def split_name(
    full_name: str,
) -> tuple[str, str]:
    first_name, last_name = full_name.split()
    return first_name, last_name
