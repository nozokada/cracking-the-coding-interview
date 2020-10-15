from linked_list import Node


def get_first_in_loop(n: Node):
    fast = n.tail.tail
    slow = n.tail
    while fast != slow:
        fast = fast.tail.tail
        slow = slow.tail

    fast = n
    while fast != slow:
        fast = fast.tail
        slow = slow.tail

    return fast
