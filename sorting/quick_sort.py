def sort(data: list, start_index: int, end_index: int):
    size = end_index - start_index + 1
    if size < 2:
        return

    pivot = data[start_index]
    i = start_index
    j = end_index

    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1

        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    sort(data, start_index, j)
    sort(data, i, end_index)


list_ = [8, 7, 6, 5, 4, 3, 2, 1]
print(list_)
sort(list_, 0, len(list_) - 1)
print(list_)
