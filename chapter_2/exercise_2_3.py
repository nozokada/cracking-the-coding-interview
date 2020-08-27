from chapter_2.exercise_2_2 import get_size
from linked_list import Node


def delete_middle(node: Node):
    size = get_size(node)
    middle_node = find_last_node_from(node, int(size / 2))
    n = middle_node
    while n is not None:
        n.data = n.tail.data
        if n.tail.tail is None:
            n.tail = None
            break
        n = n.tail


def find_last_node_from(node: Node, k: int):
    size = get_size(node)
    target_i = size - k - 1
    if target_i < 0:
        raise IndexError
    n = node
    i = 0
    while n is not None:
        if target_i == i:
            return n
        n = n.tail
        i += 1
