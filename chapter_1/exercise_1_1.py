def are_all_chars_unique(string: str):
    str_list = list(string)
    str_list.sort()
    for index in range(len(str_list) - 1):
        if str_list[index] == str_list[index + 1]:
            return False

    return True
