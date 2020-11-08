def sort(data: list):
    size = len(data)
    if size < 2:
        return data

    left = sort(data[:size // 2])
    right = sort(data[size // 2:])

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

    return data


list_ = [5, 5, 3, 5, 9, 1, 4, 5]
print(list_)
sort(list_)
print(list_)
