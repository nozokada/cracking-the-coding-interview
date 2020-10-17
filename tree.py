class Node:
    def __init__(self, data, adjacent=None):
        self.data = data
        self.adjacent = adjacent or []
        self.visited = False
