from binary_tree import BSTNode


def build_bst_from_list(ascending_list: list, root: BSTNode = None):
    if not ascending_list:
        return root

    middle_index = len(ascending_list) // 2
    middle = ascending_list.pop(middle_index)
    root = insert_node(root, None, middle)

    build_bst_from_list(ascending_list[:middle_index], root)
    build_bst_from_list(ascending_list[middle_index:], root)

    return root


def insert_node(root: BSTNode, parent: BSTNode, data: int):
    if not root:
        return BSTNode(data, parent=parent)

    if data < root.data:
        root.left = insert_node(root.left, root, data)
    else:
        root.right = insert_node(root.right, root, data)

    return root
