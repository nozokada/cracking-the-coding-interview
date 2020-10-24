from binary_tree import BSTNode


def is_balanced(root: BSTNode):
    if check_height(root) < 0:
        return False
    return True


def check_height(node: BSTNode):
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
