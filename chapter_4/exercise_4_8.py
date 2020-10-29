from bst import BSTNode


def contains_tree(t1: BSTNode, t2: BSTNode):
    if not t2:
        return True

    return check_sub_tree(t1, t2)


def check_sub_tree(r1: BSTNode, r2: BSTNode):
    if not r1:
        return False

    if r1.data == r2.data:
        if check_match_tree(r1, r2):
            return True

    return check_sub_tree(r1.left, r2) or check_sub_tree(r1.right, r2)


def check_match_tree(r1: BSTNode, r2: BSTNode):
    if not r1 and not r2:
        return True

    if not r1 or not r2:
        return False

    if r1.data != r2.data:
        return False

    return check_match_tree(r1.left, r2.left) and check_match_tree(r1.right, r2.right)
