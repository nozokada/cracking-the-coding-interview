import unittest

from chapter_1.exercise_1_1 import are_all_chars_unique
from chapter_1.exercise_1_2 import reverse, reverse_in_place
from chapter_1.exercise_1_3 import are_permutations_each_other
from chapter_1.exercise_1_4 import replace_space_with_url_encoded
from chapter_1.exercise_1_5 import compress
from chapter_1.exercise_1_6 import rotate
from chapter_1.exercise_1_7 import set_zeros
from chapter_1.exercise_1_8 import are_rotated


class Test_1_1(unittest.TestCase):
    def test_all_unique_chars(self):
        self.assertTrue(are_all_chars_unique('1234567890'))
        self.assertFalse(are_all_chars_unique('1234567891'))


class Test_1_2(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('0123456789'), '9876543210')
        self.assertEqual(reverse_in_place('0123456789'), '9876543210')


class Test_1_3(unittest.TestCase):
    def test_permutations(self):
        self.assertTrue(are_permutations_each_other('123456789', '928347561'))
        self.assertFalse(are_permutations_each_other('123456789', '928347569'))


class Test_1_4(unittest.TestCase):
    def test_url_encoded_spaces(self):
        self.assertEqual(replace_space_with_url_encoded('Mr John Smith    '), 'Mr%20John%20Smith%20%20%20%20')


class Test_1_5(unittest.TestCase):
    def test_compression(self):
        self.assertEqual(compress('aabcccccaaa'), 'a2b1c5a3')


class Test_1_6(unittest.TestCase):
    def test_matrix_rotation(self):
        self.assertEqual(rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]),
                         [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])


class Test_1_7(unittest.TestCase):
    def test_matrix_zeros(self):
        self.assertEqual(set_zeros([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]),
                         [[1, 0, 3, 4], [5, 0, 7, 8], [0, 0, 0, 0], [13, 0, 15, 16], [17, 0, 19, 20]])


class Test_1_8(unittest.TestCase):
    def test_rotated(self):
        self.assertTrue(are_rotated('waterbottle', 'erbottlewat'))
        self.assertFalse(are_rotated('waterbottle', 'eraottlewat'))
