from tree import Node


def search_dft_r(root: Node):
    if not root:
        return
    print(root.data)
    root.visited = True
    for n in root.adjacent:
        if not n.visited:
            search_dft_r(n)


def search_dft_stack(root: Node):
    stack = [root]
    while stack:
        node = stack.pop()
        node.visited = True
        print(node.data)
        for n in node.adjacent:
            if not n.visited:
                stack.append(n)


def search_bft_queue(root: Node):
    queue = [root]
    while queue:
        node = queue.pop(0)
        node.visited = True
        print(node.data)
        for n in node.adjacent:
            if not n.visited:
                queue.append(n)
