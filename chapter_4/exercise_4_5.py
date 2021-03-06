from binary_tree import TreeNode

last_value = float('-inf')


def is_bst(root: TreeNode):
    global last_value

    if not root:
        return True

    if not is_bst(root.left):
        return False

    if root.data < last_value:
        return False
    last_value = root.data

    if not is_bst(root.right):
        return False

    return True
