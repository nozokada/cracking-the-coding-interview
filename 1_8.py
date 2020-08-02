def are_rotated(str_1: str, str_2: str):
    if len(str_1) != len(str_2):
        return False

    return str_1 in str_2 * 2


test_string_1 = 'waterbottle'
test_string_2 = 'erbottlewat'
print(are_rotated(test_string_1, test_string_2))
