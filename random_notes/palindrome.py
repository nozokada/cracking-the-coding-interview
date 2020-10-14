def is_palindrome(string: str):
    for index in range(len(string) // 2):
        if string[index] != string[len(string) - 1 - index]:
            return False
    return True
