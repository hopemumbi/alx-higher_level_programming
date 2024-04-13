import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        """ Make sure type errors are raised when necessary """
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 'a'])
