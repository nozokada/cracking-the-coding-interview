def sort(data: list):
    for i in range(len(data) - 1):
        swap(data, i, find_minimum_index(data, i + 1))


def find_minimum_index(data: list, start_index: int):
    minimum_index = start_index
    minimum_value = data[start_index]
    for i in range(start_index, len(data)):
        if minimum_value > data[i]:
            minimum_value = data[i]
            minimum_index = i
    return minimum_index


def swap(data: list, index_1: int, index_2: int):
    temp = data[index_1]
    data[index_1] = data[index_2]
    data[index_2] = temp


list_ = [5, 5, 3, 5, 9, 1, 4, 5]
print(list_)
sort(list_)
print(list_)
