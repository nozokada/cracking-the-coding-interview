def all_chars_unique(string: str):
    str_list = list(string)
    str_list.sort()
    for index in range(len(str_list) - 1):
        if str_list[index] == str_list[index + 1]:
            return False
    return True


string = '1234567890'
print(list(range(len(string))))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(all_chars_unique(string))
