import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test cases for the Base class"""

    def test_emptyid(self):
        """
        Check if Base class initializes with id 1 by default
        and autoincrements
        """
        b1 = Base()
        # Asserting that the id of b1 is 1
        self.assertEqual(b1.id, 1)

    def test_emptyid_autoincrement(self):
        b1 = Base()
        b2 = Base()
        # Asserting that the id of b2 is increased by 1
        self.assertEqual(b1.id, b2.id - 1)

    def test_emptyid_autoincrement_again(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        # Asserting that the id of b3 is 3
        self.assertEqual(b2.id, b3.id-1)

    def test_unique_id(self):
        b4 = Base(12)
        # Asserting that the id of b4 is 12
        self.assertEqual(b4.id, 12)

    def test_emptyid_again(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        # Asserting that the id of b5 is 4
        self.assertEqual(b3.id, b5.id - 1)


if __name__ == '__main__':
    # Running the test cases
    unittest.main()
