class Node:
    def __init__(self, data, tail=None):
        self.data = data
        self.tail: Node = tail

    def __eq__(self, other):
        if not other:
            return False

        if type(self) != type(other):
            raise TypeError('Could not compare different types')

        if self.data != other.data:
            return False

        if not self.tail:
            if not other.tail:
                return True
            return False

        return self.tail.__eq__(other.tail)

    def append(self, data):
        new_node = Node(data)
        n = self
        while n.tail is not None:
            n = n.tail
        n.tail = new_node

        return new_node

    def delete(self, data):
        head = self
        if head.data == data:
            return head.tail

        n = head
        while n.tail is not None:
            if n.tail.data == data:
                n.tail = n.tail.tail
                return head
            n = n.tail

        return head

    def print(self):
        if self.tail is None:
            return f'{self.data}'
        return f'{self.data} -> {self.tail.print()}'
