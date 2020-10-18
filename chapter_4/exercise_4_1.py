from binary_tree import Node


def is_balanced(root: Node):
    if check_height(root) < 0:
        return False
    return True


def check_height(node: Node):
    if not node:
        return 0

    left_height = check_height(node.left)
    right_height = check_height(node.right)

    if left_height < 0 or right_height < 0:
        return -1

    diff = abs(left_height - right_height)

    if diff > 1:
        return -1

    return max(left_height, right_height) + 1
