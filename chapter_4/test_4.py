import unittest

from binary_tree import Node
from chapter_4.exercise_4_1 import is_balanced
from chapter_4.exercise_4_2 import is_route
from chapter_4.traversal import do_dfs_r


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = Node(1,
                         Node(2,
                              Node(3,
                                   Node(4), Node(5)),
                              Node(6,
                                   Node(7), Node(8))),
                         Node(9,
                              Node(10,
                                   Node(11), Node(12)),
                              Node(13,
                                   Node(14), Node(15))))

    def test_print(self):
        self.tree.print()
        print()

    def test_traverse(self):
        self.tree.traverse(do_dfs_r)


class Test_4_1(unittest.TestCase):
    def test_is_balanced(self):
        tree = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
        another_tree = Node(1, Node(2, Node(3), Node(4)))
        self.assertTrue(is_balanced(tree))
        self.assertFalse(is_balanced(another_tree))


class Test_4_2(unittest.TestCase):
    def test_is_route(self):
        end = Node(7)
        start_false = Node(4)
        start_true = Node(1, Node(2, Node(3), start_false), Node(5, Node(6), end))
        self.assertTrue(is_route(start_true, end))
        self.assertFalse(is_route(start_false, end))
