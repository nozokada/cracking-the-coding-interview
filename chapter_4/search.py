from binary_tree import Node


def do_dfs_r(root: Node):
    if not root:
        return
    print(root.data)
    root.visited = True
    for n in root.adjacent:
        if not n.visited:
            do_dfs_r(n)


def do_dfs_stack(root: Node):
    root.visited = True
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data)
        for n in node.adjacent:
            if not n.visited:
                n.visited = True
                stack.append(n)


def do_bfs_queue(root: Node):
    root.visited = True
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data)
        for n in node.adjacent:
            if not n.visited:
                n.visited = True
                queue.append(n)
