def sort(data: list):
    for which in range(1, len(data)):
        val = data[which]
        for i in range(which):
            if data[i] > val:
                shift_to_right(data, i, which - i)
                data[i] = val
                break


def shift_to_right(data: list, start_index: int, count: int):
    end_index = start_index + count
    if end_index > len(data) - 1:
        raise IndexError
    for i in range(end_index, start_index - 1, -1):
        data[i] = data[i - 1]


list_ = [5, 5, 3, 5, 9, 1, 4, 5]
print(list_)
sort(list_)
print(list_)
