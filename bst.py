class TreeNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.visited = False

    @property
    def adjacent(self):
        return [n for n in (self.left, self.right) if n]

    def print_structure(self):
        string = ""
        current_level = [self]
        height = get_height(self)
        while height > 0:
            next_level = []
            padding = 2 ** (height - 1) - 1
            for n in current_level:
                string += " " * padding
                if not n:
                    string += " "
                    next_level.append(None)
                    next_level.append(None)
                else:
                    string += f'{n.data}'
                    next_level.append(n.left)
                    next_level.append(n.right)
                string += " " * (padding + 1)
            string += "\n"
            current_level = next_level
            height -= 1
        return string

    def traverse(self, traverse_func):
        traverse_func(self)

    def __str__(self):
        return f'{self.data}'


def get_height(root: TreeNode):
    if not root:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1
