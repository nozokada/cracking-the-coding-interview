from linked_list import Node


def partition(value: int, node: Node):
    smaller_nodes = None
    bigger_nodes = None
    partition_node = None

    n = node
    while n is not None:
        if n.data >= value:
            if bigger_nodes is None:
                bigger_nodes = Node(n.data)
            else:
                bigger_nodes.append(n.data)
        else:
            if smaller_nodes is None:
                smaller_nodes = Node(n.data)
                partition_node = smaller_nodes
            else:
                partition_node = smaller_nodes.append(n.data)
        n = n.tail

    if smaller_nodes is None:
        return bigger_nodes

    partition_node.tail = bigger_nodes
    return smaller_nodes
