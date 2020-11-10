def sort(data: list, start_index: int, end_index: int):
    size = end_index - start_index + 1
    if size < 2:
        return

    pivot = data[start_index]
    i = start_index
    j = end_index

    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1

        if i >= j:
            break

        data[i], data[j] = data[j], data[i]

        i += 1
        j -= 1

    sort(data, start_index, i - 1)
    sort(data, j + 1, end_index)


list_ = [5, 5, 3, 5, 9, 1, 4, 5]
print(list_)
sort(list_, 0, len(list_) - 1)
print(list_)
