class Node:
    def __init__(self, data: int, tail=None):
        self.data: int = data
        self.tail: Node = tail

    def append(self, data: int):
        end = Node(data)
        node = self
        while node.tail is not None:
            node = node.tail
        node.tail = end

    def delete(self, data: int):
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


linked_list = Node(1, Node(2, Node(3, Node(4))))

linked_list.append(5)
print(linked_list.get_data())

another_linked_list = linked_list.delete(1)
print(another_linked_list.get_data())
