def are_permutations_each_other(str_1: str, str_2: str):
    if len(str_1) != len(str_2):
        return False

    counter = {}
    for char in str_1:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    for char in str_2:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1
        # print(counter)

    return True

