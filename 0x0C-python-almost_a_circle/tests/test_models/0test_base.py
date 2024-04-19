import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """
    Test cases for the Base class
    """

    def test_empty_id_default(self):
        """
        Test case to check if Base class initializes with id 1 by default
        """
        b1 = Base()
        # Asserting that the id of b1 is 1
        self.assertEqual(b1.id, 1)

    def test_empty_id_auto_increment(self):
        """
        Test case to check if Base class auto-increments ids correctly
        """
        b1 = Base()
        b2 = Base()
        # Asserting that the id of b2 is 2 (due to auto-incrementing)
        self.assertEqual(b2.id, 2)

    def test_empty_id_auto_increment_again(self):
        """
        Test case to check if Base class continues auto-incrementing ids correctly
        after other instances have been created
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        # Asserting that the id of b3 is 3 (due to auto-incrementing)
        self.assertEqual(b3.id, 3)

    def test_non_empty_id(self):
        """
        Test case to check if Base class initializes with a provided non-empty id
        """
        b4 = Base(12)
        # Asserting that the id of b4 is 12
        self.assertEqual(b4.id, 12)

    def test_empty_id_auto_increment(self):
        """
        Test case to check if Base class auto-increments ids correctly even after other instances have been created
        """
        b5 = Base()
        # Asserting that the id of b5 is 4 (due to auto-incrementing)
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    # Running the test cases
    unittest.main()

