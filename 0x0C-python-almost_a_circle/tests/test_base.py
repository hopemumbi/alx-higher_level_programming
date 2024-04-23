import unittest
from models.base import Base
from models.rectangle import Rectangle


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


class TestBase_to_json_string(unittest.TestCase):
    """Test cases for method to_json_string() of class base"""

    def test_to_json_string_with_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_dictionary_type(self):
        r1 = Rectangle(10, 7, 2, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_string_with_list_of_dictionaries(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = '[{"id": 6, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, expected)


if __name__ == '__main__':
    # Running the test cases
    unittest.main()
