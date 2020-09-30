from linked_list import Node


def find_sum(node_1: Node, node_2: Node):
    n_1 = node_1
    n_2 = node_2
    n_result = None
    carryover = 0

    while n_1 or n_2:
        d_1 = n_1.data if n_1 else 0
        d_2 = n_2.data if n_2 else 0

        total = d_1 + d_2 + carryover
        d_result = total % 10
        carryover = total // 10

        if n_result:
            n_result.append(d_result)
        else:
            n_result = Node(d_result)

        n_1 = n_1.tail if n_1 else None
        n_2 = n_2.tail if n_2 else None

    return n_result
