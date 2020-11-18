from binary_tree import TreeNode


def get_next_node_in_order(node: TreeNode):
    n = node
    if not n:
        return None

    if n.right:
        n = n.right
        while n.left:
            n = n.left
    else:
        data = n.data
        while n and n.data <= data:
            n = n.parent
    return n
