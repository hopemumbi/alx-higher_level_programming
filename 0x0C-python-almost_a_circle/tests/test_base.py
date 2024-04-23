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


class TestBase_from_json_string(unittest.TestCase):
    """Test cases for method from_json_string() of class base"""

    def test_from_json_string_with_empty_string(self):
        json_string = ""
        got = Rectangle.from_json_string(json_string)
        self.assertEqual(got, [])

    def test_from_json_string_with_none(self):
        json_string = []
        got = Rectangle.from_json_string(json_string)
        self.assertEqual(got, [])

    def test_from_json_string_with_valid_json_string(self):
        list_dict = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_string = Rectangle.to_json_string(list_dict)
        got = Rectangle.from_json_string(json_string)
        self.assertEqual(got, list_dict)


class TestBase_save_to_file(unittest.TestCase):
    """Test cases for method; save_to_file()"""

    def test_save_list_of_instances(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            read = file.read()

        expected = (
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
                '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        )

        self.assertEqual(read, expected)

    def test_save_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            read = file.read()
        expected = '[]'
        self.assertEqual(read, expected)


class TestBase_create(unittest.TestCase):
    """Test cases for method; create(cls, **dictionary)"""

    def test_create_an_instance(self):
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)


if __name__ == '__main__':
    # Running the test cases
    unittest.main()
