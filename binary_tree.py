class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.visited = False

    @property
    def adjacent(self):
        return [n for n in (self.left, self.right) if n]

    def print(self):
        print_binary_tree(self)


def print_binary_tree(root: Node):
    current_level = [root]
    height = get_height(root)
    padding = 2 ** (height - 1) - 1
    while True:
        if height == 0:
            break
        next_level = []
        for n in current_level:
            print(" " * padding, end='')
            if not n:
                print(" ", end='')
            else:
                print(n.data, end='')
                next_level.append(n.left)
                next_level.append(n.right)
            print(" " * (padding + 1), end='')
        print()
        current_level = next_level
        height -= 1
        padding = 2 ** (height - 1) - 1


def get_height(root: Node):
    if not root:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1
