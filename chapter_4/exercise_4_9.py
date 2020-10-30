from bst import BSTNode, get_height


def find_sum(root: BSTNode, value: int):
    path = []
    for i in range(get_height(root)):
        path.append(float('-inf'))
    traverse_and_find_sum(root, value, path, 0)


def traverse_and_find_sum(node: BSTNode, value: int, path: list, level: int):
    if not node:
        return

    path[level] = node.data
    sum_value = 0
    for i in range(level, -1, -1):
        sum_value += path[i]
        if sum_value == value:
            print(path[i:level + 1])

    traverse_and_find_sum(node.left, value, path, level + 1)
    traverse_and_find_sum(node.right, value, path, level + 1)
