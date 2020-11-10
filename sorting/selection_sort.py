def sort(data: list):
    for i in range(len(data) - 1):
        min_value_index = find_minimum_index(data, i + 1)
        data[i], data[min_value_index] = data[min_value_index], data[i]


def find_minimum_index(data: list, start_index: int):
    min_index = start_index
    min_value = data[start_index]
    for i in range(start_index, len(data)):
        if min_value > data[i]:
            min_value = data[i]
            min_index = i
    return min_index


list_ = [5, 5, 3, 5, 9, 1, 4, 5]
print(list_)
sort(list_)
print(list_)
