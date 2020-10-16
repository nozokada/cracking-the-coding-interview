from linked_list import Node


def is_palindrome(n: Node):
    fast = n
    slow = n
    stack = []
    while fast and fast.tail:
        stack.append(slow.data)
        fast = fast.tail.tail
        slow = slow.tail

    if fast:
        slow = slow.tail

    while slow.tail:
        if slow.data != stack.pop():
            return False
        slow = slow.tail
    return True
