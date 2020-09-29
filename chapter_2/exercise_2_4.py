from linked_list import Node


def partition(value: int, node: Node):
    n_smaller = None
    n_bigger = None
    n_partition = None

    n = node
    while n:
        if n.data >= value:
            if n_bigger:
                n_bigger.append(n.data)
            else:
                n_bigger = Node(n.data)
        else:
            if n_smaller:
                n_partition = n_smaller.append(n.data)
            else:
                n_smaller = Node(n.data)
                n_partition = n_smaller
        n = n.tail

    if not n_smaller:
        return n_bigger

    n_partition.tail = n_bigger
    return n_smaller
