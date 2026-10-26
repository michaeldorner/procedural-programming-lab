def split_name(
    full_name: str,
) -> tuple[str, str]:
    first_name, last_name = full_name.split()
    return first_name, last_name
