import unittest

from bst import BSTNode
from chapter_4.exercise_4_1 import is_balanced
from chapter_4.exercise_4_2 import is_route
from chapter_4.exercise_4_3 import build_bst_from_list
from chapter_4.exercise_4_4 import create_linked_lists
from chapter_4.exercise_4_5 import is_bst
from chapter_4.exercise_4_6 import get_next_node_in_order
from chapter_4.exercise_4_7 import find_common_ancestor
from chapter_4.exercise_4_8 import contains_tree
from chapter_4.exercise_4_9 import find_sum
from chapter_4.traversal import do_dfs_r


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BSTNode(1,
                            BSTNode(2,
                                    BSTNode(3,
                                            BSTNode(4), BSTNode(5)),
                                    BSTNode(6,
                                            BSTNode(7), BSTNode(8))),
                            BSTNode(9,
                                    BSTNode(10,
                                            BSTNode(11), BSTNode(12)),
                                    BSTNode(13,
                                            BSTNode(14), BSTNode(15))))

    def test_print(self):
        print(self.tree.print_structure())

    def test_traverse(self):
        self.tree.traverse(do_dfs_r)


class Test_4_1(unittest.TestCase):
    def test_is_balanced(self):
        tree = BSTNode(1, BSTNode(2, BSTNode(3), BSTNode(4)), BSTNode(5, BSTNode(6), BSTNode(7)))
        another_tree = BSTNode(1, BSTNode(2, BSTNode(3), BSTNode(4)))
        self.assertTrue(is_balanced(tree))
        self.assertFalse(is_balanced(another_tree))


class Test_4_2(unittest.TestCase):
    def test_is_route(self):
        end = BSTNode(7)
        start_false = BSTNode(4)
        start_true = BSTNode(1, BSTNode(2, BSTNode(3), start_false), BSTNode(5, BSTNode(6), end))
        self.assertTrue(is_route(start_true, end))
        self.assertFalse(is_route(start_false, end))


class Test_4_3(unittest.TestCase):
    def test_build_bst_from_list(self):
        tree = build_bst_from_list([n for n in range(10)])
        print(tree.print_structure())


class Test_4_4(unittest.TestCase):
    def test_create_linked_lists(self):
        tree = BSTNode(1, BSTNode(2, BSTNode(3), BSTNode(4)), BSTNode(5, BSTNode(6), BSTNode(7)))
        linked_lists = create_linked_lists(tree)
        for linked_list in linked_lists:
            print(linked_list.print_structure())


class Test_4_5(unittest.TestCase):
    def test_is_bst(self):
        bst = build_bst_from_list([n for n in range(1, 16)])
        tree = BSTNode(1, BSTNode(2, BSTNode(3), BSTNode(4)), BSTNode(5, BSTNode(6), BSTNode(7)))
        print(bst.print_structure())
        print(tree.print_structure())
        self.assertTrue(is_bst(bst))
        self.assertFalse(is_bst(tree))


class Test_4_6(unittest.TestCase):
    def test_get_next_node_in_order(self):
        bst = build_bst_from_list([n for n in range(1, 16)])
        node = get_next_node_in_order(bst.right.right)
        next_node = get_next_node_in_order(node)
        print(bst.print_structure())
        print(next_node)


class Test_4_7(unittest.TestCase):
    def test_find_first_common_ancestor(self):
        node_1 = BSTNode(4)
        node_2 = BSTNode(7)
        tree = BSTNode(1, BSTNode(2, BSTNode(3), node_1), BSTNode(5, BSTNode(6), node_2))
        self.assertEqual(tree, find_common_ancestor(tree, node_1, node_2))


class Test_4_8(unittest.TestCase):
    def test_contains_tree(self):
        big_tree = BSTNode(1, BSTNode(2, BSTNode(3), BSTNode(4)), BSTNode(5, BSTNode(6), BSTNode(7)))
        small_tree = BSTNode(5, BSTNode(6), BSTNode(7))
        self.assertTrue(contains_tree(big_tree, small_tree))


class Test_4_9(unittest.TestCase):
    def test_find_sum(self):
        tree = BSTNode(1, BSTNode(2, BSTNode(3), BSTNode(4)), BSTNode(5, BSTNode(6), BSTNode(7)))
        print(tree.print_structure())
        find_sum(tree, 3)
