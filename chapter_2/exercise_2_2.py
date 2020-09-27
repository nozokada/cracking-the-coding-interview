from linked_list import Node


def get_size(node: Node):
    n = node
    size = 0
    while n:
        size += 1
        n = n.tail
    return size


def find_last_element_from(node: Node, k: int):
    size = get_size(node)
    target_i = size - k - 1
    if target_i < 0:
        raise IndexError
    n = node
    i = 0
    while n:
        if target_i == i:
            return n.data
        n = n.tail
        i += 1
