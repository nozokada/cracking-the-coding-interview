from binary_tree import Node


def do_dfs_r(root: Node):
    if not root:
        return
    print(root.data, end=' ')
    do_dfs_r(root.left)
    do_dfs_r(root.right)


def do_dfs_stack(root: Node):
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        print(node.data, end=' ')
        stack.append(node.left)
        stack.append(node.right)


def do_bfs_queue(root: Node):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node:
            continue
        print(node.data, end=' ')
        queue.append(node.left)
        queue.append(node.right)
