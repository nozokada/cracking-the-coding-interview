class Node:
    def __init__(self, data, tail=None):
        self.data = data
        self.tail: Node = tail

    def __eq__(self, other):
        if other is None:
            return False

        if self.data != other.data:
            return False

        if self.tail is None:
            if other.tail is None:
                return True
            return False

        return self.tail.__eq__(other.tail)

    def append(self, data):
        end = Node(data)
        node = self
        while node.tail is not None:
            node = node.tail
        node.tail = end

    def delete(self, data):
        head = self
        node = head
        if node.data == data:
            return node.tail
        while node.tail is not None:
            if node.tail.data == data:
                node.tail = node.tail.tail
                return head
            node = node.tail
        return head

    def get_data(self):
        if self.tail is None:
            return f'{self.data}'
        return f'{self.data} -> {self.tail.get_data()}'
