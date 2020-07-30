def replace_space_with_url_encoded(string: str):
    str_list = list(string)
    for index in range(len(str_list)):
        if str_list[index].isspace():
            str_list[index] = '%20'
    return ''.join(str_list)


test_string = 'Mr John Smith    '
print(replace_space_with_url_encoded(test_string))
