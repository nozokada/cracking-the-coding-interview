from chapter_2.exercise_2_2 import get_size
from linked_list import Node


def find_sum(n_1: Node, n_2: Node):
    n_result = None
    carryover = 0

    while n_1 or n_2:
        d_1 = n_1.data if n_1 else 0
        d_2 = n_2.data if n_2 else 0

        total = d_1 + d_2 + carryover
        result = total % 10
        carryover = total // 10

        if n_result:
            n_result.append(result)
        else:
            n_result = Node(result)

        n_1 = n_1.tail if n_1 else None
        n_2 = n_2.tail if n_2 else None

    return n_result


def find_sum_reverse(n_1: Node, n_2: Node):
    diff = get_size(n_1) - get_size(n_2)
    for i in range(abs(diff)):
        if diff < 0:
            n_1 = add_leading_zero(n_1)
        else:
            n_2 = add_leading_zero(n_2)

    n, carryover = find_sum_r(n_1, n_2)
    if carryover > 0:
        n_result = Node(carryover)
        n_result.tail = n
        return n_result
    return n


def add_leading_zero(n: Node):
    n_zero = Node(0)
    n_zero.tail = n
    return n_zero


def find_sum_r(n_1: Node, n_2: Node):
    d_1 = n_1.data
    d_2 = n_2.data

    if not n_1.tail or not n_2.tail:
        total = d_1 + d_2
        result = total % 10
        carryover = total // 10
        return Node(result), carryover

    n, carryover = find_sum_r(n_1.tail, n_2.tail)
    total = d_1 + d_2 + carryover
    result = total % 10
    carryover = total // 10

    n_result = Node(result)
    n_result.tail = n
    return n_result, carryover
