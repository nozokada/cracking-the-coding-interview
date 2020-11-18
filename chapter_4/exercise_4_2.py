from binary_tree import TreeNode


def is_route(start: TreeNode, end: TreeNode):
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
