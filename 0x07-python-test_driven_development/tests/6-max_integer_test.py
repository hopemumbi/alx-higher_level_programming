import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_one_number(self):
        self.assertEqual(max_integer([3]), 3)

    def test_duplicate_number(self):
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)


    def test_non_integers(self):
        """ Make sure type errors are raised when necessary """
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 'a'])
