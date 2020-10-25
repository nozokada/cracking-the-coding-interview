from binary_tree import BSTNode
from linked_list import Node


def create_linked_lists(root: BSTNode):
    result = []
    current_linked_list = Node(root)

    while current_linked_list:
        result.append(current_linked_list)
        n = current_linked_list
        next_linked_list: Node = None

        while n:
            if n.data.left:
                if next_linked_list:
                    next_linked_list.append(n.data.left)
                else:
                    next_linked_list = Node(n.data.left)
            if n.data.right:
                if next_linked_list:
                    next_linked_list.append(n.data.right)
                else:
                    next_linked_list = Node(n.data.right)
            n = n.tail

        current_linked_list = next_linked_list

    return result
