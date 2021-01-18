class Node:
    def __init__(self, data, tail=None):
        self.data = data
        self.tail: Node = tail

    def __eq__(self, other):
        if id(self) == id(other):
            return True

        if not isinstance(other, Node):
            return False

        if self.data != other.data:
            return False

        return self.tail == other.tail

    def append(self, data):
        append_me = Node(data)
        n = self
        while n:
            if not n.tail:
                n.tail = append_me
                return append_me
            n = n.tail

    def delete(self, delete_me):
        if self == delete_me:
            return self.tail
        n = self
        while n:
            if n.tail == delete_me:
                n.tail = delete_me.tail
                return self
            n = n.tail

    def reverse(self):
        if not self.tail:
            return self
        prev = None
        curr = self

        while curr:
            next = curr.tail
            curr.tail = prev

            prev = curr
            curr = next
        return prev

    def print_structure(self):
        if not self.tail:
            return f'{self.data}'
        return f'{self.data} -> {self.tail.print_structure()}'

    def __str__(self):
        return f'{self.data}'
