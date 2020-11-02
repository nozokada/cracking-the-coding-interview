def longest_subarray(arr):
    max_value = arr[0]
    min_value = arr[0]
    prev = arr[0]
    max_length = 0
    count = 1
    same_count = 1

    for i in range(1, len(arr)):
        value = arr[i]
        max_value = max(value, max_value)
        min_value = min(value, min_value)

        if max_value - min_value > 1:
            max_length = max(max_length, count)
            count = same_count + 1 if abs(value - prev) == 1 else 1
            max_value = value
            min_value = value
        else:
            count += 1

        same_count = same_count + 1 if value == prev else 1
        prev = value

    max_length = max(max_length, count)

    return max_length


arr_1 = [3, 2, 2, 2, 2, 1, 1]
arr_2 = [2, 2, 1]
arr_3 = [1, 1, 1, 3, 3, 2, 2, 1, 1]
print(longest_subarray(arr_3))
