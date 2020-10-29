from bst import BSTNode


def find_common_ancestor(root: BSTNode, p: BSTNode, q: BSTNode):
    if not is_ancestor(root, p) or not is_ancestor(root, q):
        return None

    return find_common_ancestor_helper(root, p, q)


def find_common_ancestor_helper(root: BSTNode, p: BSTNode, q: BSTNode):
    if not root:
        return None

    if root == p or root == q:
        return root

    p_is_on_left = is_ancestor(root.left, p)
    q_is_on_left = is_ancestor(root.left, q)

    if p_is_on_left != q_is_on_left:
        return root

    child_side = root.left if p_is_on_left else root.right
    return find_common_ancestor_helper(child_side, p, q)


def is_ancestor(node: BSTNode, child: BSTNode):
    if not node:
        return False

    if node == child:
        return True

    return is_ancestor(node.left, child) or is_ancestor(node.right, child)
