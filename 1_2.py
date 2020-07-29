def reverse(string: str):
    str_list = []
    for index in range(len(string) - 1, -1, -1):
        str_list.append(string[index])
    return ''.join(str_list)


def reverse_in_place(string: str):
    str_list = list(string)
    for index in range(int(len(str_list) / 2)):
        tmp = str_list[index]
        str_list[index] = str_list[len(str_list) - 1 - index]
        str_list[len(str_list) - 1 - index] = tmp
    return ''.join(str_list)


test_string = '0123456789'
print(reverse(test_string))
print(list(range(int(len(test_string) / 2))))  # [0, 1, 2, 3, 4]
print(reverse_in_place(test_string))
