from binary_tree import Node


def search_dft_r(root: Node):
    if not root:
        return
    print(root.data)
    root.visited = True
    for n in root.adjacent:
        if not n.visited:
            search_dft_r(n)


def search_dft_stack(root: Node):
    root.visited = True
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data)
        for n in node.adjacent:
            if not n.visited:
                node.visited = True
                stack.append(n)


def search_bft_queue(root: Node):
    root.visited = True
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data)
        for n in node.adjacent:
            if not n.visited:
                node.visited = True
                queue.append(n)


tree = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
search_bft_queue(tree)
