import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Test cases for the Rectangle class """

    def test_rectangle_id(self):
        """Test case to check if Rectangle class assigns correct ids"""
        # Create instance of Rectangle with no id assigned
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        # Create instance of Rectangle with no id assigned
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        # Create instance of Rectangle with no id=12
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


if __name__ == "__main__":
    unittest.main()
