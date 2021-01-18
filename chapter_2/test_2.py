import unittest

from chapter_2.exercise_2_5 import find_sum, find_sum_reverse
from chapter_2.exercise_2_1 import delete_duplicates, delete_duplicates_in_place
from chapter_2.exercise_2_2 import find_last_element_from, get_size
from chapter_2.exercise_2_3 import delete_middle
from chapter_2.exercise_2_4 import partition
from chapter_2.exercise_2_6 import get_first_in_loop
from chapter_2.exercise_2_7 import is_palindrome
from linked_list import Node


class TestLinkedList(unittest.TestCase):
    def test_linked_list_equal(self):
        self.assertEqual(Node(1, Node(2, Node(3, Node(4)))), Node(1, Node(2, Node(3, Node(4)))))
        self.assertNotEqual(Node(1, Node(2, Node(3, Node(4)))), Node(1, Node(2, Node(3, Node(5)))))

    def test_linked_list_append(self):
        linked_list = Node(1, Node(2, Node(3, Node(4))))
        another_linked_list = Node(1, Node(2, Node(3)))
        another_linked_list.append(4)
        self.assertEqual(linked_list, another_linked_list)

    def test_linked_list_delete(self):
        linked_list = Node(1, Node(2, Node(3)))
        delete_me = Node(4)
        another_linked_list = Node(1, Node(2, Node(3, delete_me)))
        another_linked_list = another_linked_list.delete(delete_me)
        self.assertEqual(linked_list, another_linked_list)

    def test_linked_list_reverse(self):
        linked_list = Node(1, Node(2, Node(3)))
        another_linked_list = Node(3, Node(2, Node(1)))
        self.assertEqual(linked_list.reverse(), another_linked_list)


class Test_2_1(unittest.TestCase):
    def test_delete_duplicates(self):
        linked_list = Node(1, Node(2, Node(3, Node(1))))
        self.assertEqual(Node(1, Node(2, Node(3))), delete_duplicates(linked_list))
        self.assertEqual(Node(1, Node(2, Node(3))), delete_duplicates_in_place(linked_list))


class Test_2_2(unittest.TestCase):
    def test_find_last_element_from(self):
        linked_list = Node(1, Node(2, Node(3, Node(4))))
        self.assertEqual(4, get_size(linked_list))
        self.assertEqual(4, find_last_element_from(linked_list, 0))


class Test_2_3(unittest.TestCase):
    def test_delete_middle(self):
        linked_list = Node("a", Node("b", Node("c", Node("d", Node("e")))))
        delete_middle(linked_list)
        self.assertEqual(Node("a", Node("b", Node("d", Node("e")))), linked_list)


class Test_2_4(unittest.TestCase):
    def test_partition(self):
        linked_list = Node(4, Node(2, Node(3, Node(1))))
        another_linked_list = Node(4, Node(5, Node(6, Node(7))))
        self.assertEqual(Node(2, Node(1, Node(4, Node(3)))), partition(3, linked_list))
        self.assertEqual(Node(4, Node(5, Node(6, Node(7)))), partition(9, another_linked_list))


class Test_2_5(unittest.TestCase):
    def test_find_sum(self):
        linked_list = Node(7, Node(1, Node(6, Node(1))))
        another_linked_list = Node(5, Node(9, Node(2)))
        self.assertEqual(Node(2, Node(1, Node(9, Node(1)))), find_sum(linked_list, another_linked_list))

    def test_find_sum_reverse(self):
        linked_list = Node(6, Node(1, Node(7)))
        another_linked_list = Node(1, Node(2, Node(9, Node(5))))
        self.assertEqual(Node(1, Node(9, Node(1, Node(2)))), find_sum_reverse(linked_list, another_linked_list))


class Test_2_6(unittest.TestCase):
    def test_get_first_in_loop(self):
        first_node_in_loop = Node('C')
        linked_list = Node('A', Node('B', first_node_in_loop))
        first_node_in_loop.tail = Node('D', Node('E', first_node_in_loop))
        self.assertEqual(first_node_in_loop.data, get_first_in_loop(linked_list).data)


class Test_2_7(unittest.TestCase):
    def test_palindrome(self):
        linked_list = Node('A', Node('B', Node('C', Node('C', Node('B', Node('A'))))))
        another_linked_list = Node('A', Node('B', Node('C', Node('B', Node('A')))))
        self.assertTrue(is_palindrome(linked_list))
        self.assertTrue(is_palindrome(another_linked_list))
