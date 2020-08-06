def compress(string: str):
    result_str_list = []
    prev_char = string[0]
    count = 1
    for index in range(1, len(string)):
        if string[index] == prev_char:
            count += 1
        else:
            result_str_list.append(f'{prev_char}{count}')
            prev_char = string[index]
            count = 1
    result_str_list.append(f'{prev_char}{count}')
    result_string = ''.join(result_str_list)

    return result_string if len(result_string) < len(string) else string
