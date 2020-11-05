def str_to_int(str_: str):
    i = 0
    num = 0
    is_negative = False
    if str_[i] == '-':
        is_negative = True
        i += 1

    while i < len(str_):
        num *= 10
        num += ord(str_[i]) - ord('0')
        i += 1

    return -num if is_negative else num


def int_to_str(int_: int):
    str_list = []
    is_negative = False
    if int_ < 0:
        int_ = -int_
        is_negative = True

    while int_ != 0:
        str_list.append(int_ % 10)
        int_ //= 10

    if is_negative:
        str_list.append('-')

    return ''.join(map(str, str_list[::-1]))


print(str_to_int('-345'))
print(int_to_str(-345))
