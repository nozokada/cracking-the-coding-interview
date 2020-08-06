def are_rotated(str_1: str, str_2: str):
    if len(str_1) != len(str_2):
        return False

    return str_1 in str_2 * 2
