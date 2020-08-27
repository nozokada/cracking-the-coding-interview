import unittest

from chapter_2.exercise_2_1 import delete_duplicates, delete_duplicates_in_place
from chapter_2.exercise_2_2 import find_last_element_from, get_size
from chapter_2.exercise_2_3 import find_last_node_from, delete_middle
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
        another_linked_list = Node(1, Node(2, Node(3, Node(4))))
        another_linked_list.delete(4)
        self.assertEqual(linked_list, another_linked_list)


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
