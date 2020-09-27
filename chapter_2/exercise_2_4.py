from linked_list import Node


def partition(value: int, node: Node):
    smaller_nodes = None
    bigger_nodes = None
    partition_node = None

    n = node
    while n:
        if n.data >= value:
            if bigger_nodes:
                bigger_nodes.append(n.data)
            else:
                bigger_nodes = Node(n.data)
        else:
            if smaller_nodes:
                partition_node = smaller_nodes.append(n.data)
            else:
                smaller_nodes = Node(n.data)
                partition_node = smaller_nodes
        n = n.tail

    if not smaller_nodes:
        return bigger_nodes

    partition_node.tail = bigger_nodes
    return smaller_nodes
