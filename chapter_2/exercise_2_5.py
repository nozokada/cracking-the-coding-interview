from linked_list import Node


def add_elements(node_1: Node, node_2: Node):
    n_1 = node_1
    n_2 = node_2
    result_node = None
    carry_over = 0

    while n_1 or n_2:
        n_1_digit = n_1.data if n_1 else 0
        n_2_digit = n_2.data if n_2 else 0

        total_num = n_1_digit + n_2_digit + carry_over
        result_digit = total_num % 10
        carry_over = total_num // 10

        if result_node:
            result_node.append(result_digit)
        else:
            result_node = Node(result_digit)

        n_1 = n_1.tail if n_1 else None
        n_2 = n_2.tail if n_2 else None

    return result_node
