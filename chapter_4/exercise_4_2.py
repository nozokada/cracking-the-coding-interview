from binary_tree import Node


def is_route(start: Node, end: Node):
    start.visited = True
    queue = [start]
    while queue:
        node = queue.pop(0)
        for n in node.adjacent:
            if n == end:
                return True
            if not n.visited:
                node.visited = True
                queue.append(n)

    return False
