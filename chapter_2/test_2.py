import unittest

from chapter_2.exercise_2_1 import delete_duplicates
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
    def test_delete_duplicates_in_linked_list(self):
        linked_list = Node(1, Node(2, Node(3, Node(1))))
        self.assertEqual(delete_duplicates(linked_list), Node(1, Node(2, Node(3))))
