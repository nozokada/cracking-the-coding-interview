from linked_list import Node


def delete_duplicates(node: Node):
    n = node
    duplicates_set = {node.data}
    while n.tail is not None:
        if n.tail.data in duplicates_set:
            n.tail = n.tail.tail
            continue
        n = n.tail
        duplicates_set.add(n.data)

    return node


def delete_duplicates_in_place(node: Node):
    i = node
    while i.tail is not None:
        j = i
        while j.tail is not None:
            if i.data == j.tail.data:
                j.tail = j.tail.tail
                continue
            j = j.tail
        i = i.tail

    return node
