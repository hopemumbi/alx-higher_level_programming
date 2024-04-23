#!/usr/bin/python3
"""Defines unittests for models/rectangle.py
"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstatiation(unittest.TestCase):
    """ Test cases for the Rectangle initialization """

    def test_inheritance(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id-1)

    def test_three_args(self):
        r1 = Rectangle(10, 2, 0)
        r2 = Rectangle(2, 10, 0)
        self.assertEqual(r1.id, r2.id-1)

    def test_four_args(self):
        r1 = Rectangle(10, 2, 0, 0)
        r2 = Rectangle(2, 10, 0, 0)
        self.assertEqual(r1.id, r2.id-1)

    def test_five_arg(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_more_than_five_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 0, 0, 0)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2).__width

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2).__height

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2).__x

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2).__y

    def test_width_getter(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    def test_width_setter(self):
        r1 = Rectangle(10, 2)
        r1.width = 11
        self.assertEqual(r1.width, 11)

    def test_height_getter(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

    def test_height_setter(self):
        r1 = Rectangle(10, 2)
        r1.height = 3
        self.assertEqual(r1.height, 3)

    def test_x_getter(self):
        r1 = Rectangle(10, 2, 0)
        self.assertEqual(r1.x, 0)

    def test_x_setter(self):
        r1 = Rectangle(10, 2, 0)
        r1.x = 1
        assertEqual(r1.x, 1)

    def test_y_getter(self):
        r1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r1.y, 0)

    def test_x_setter(self):
        r1 = Rectangle(10, 2, 0, 0)
        r1.y = 1
        self.assertEqual(r1.y, 1)


class TestWidthValidation(unittest.TestCase):
    """Test cases for Rectangle width."""

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.5, 2)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10j, 2)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([9, 10], 2)

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((9, 10), 2)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"nine": 9, "ten": 10}, 2)

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({9, 10}, 2)

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 2)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)


class TestHeightValidation(unittest.TestCase):
    """Test cases for Rectangle height. """

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_int_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.5)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2j)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [1, 2])

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (1, 2))

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {"one": 1, "two": 2})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {1, 2})

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)


class TestXValidation(unittest.TestCase):
    """Test cases for Rectangle x-coordinate"""
    def test_int_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 3.5)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 3j)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [2, 3])

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, (2, 3))

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {"two": 2, "three": 3})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {2, 3})

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, True)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None)


class TestYValidation(unittest.TestCase):
    """Test cases for Rectangle y-coordinate """

    def test_int_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "1")

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, 1.5)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, 1j)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, [0, 1])

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, (0, 1))

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, {"Zero": 0, "One": 1})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, {0, 1})

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, True)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, None)


class TestVAlidationOrder(unittest.TestCase):
    """Test cases for order of validaton"""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", "2", 3, 1)

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2, "3", 1)

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2, 3, "1")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2", "3", 1)

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2", 3, "1")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3", "1")


class TestRectangleArea(unittest.TestCase):
    """Test cases for area of rectangle"""

    def test_small(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_large(self):
        r2 = Rectangle(1000000000000000, 1000000000000000)
        self.assertEqual(r2.area(), 1000000000000000000000000000000)

    def test_change_of_variable(self):
        r3 = Rectangle(10, 2, 0, 0, 0)
        r3.width = 8
        r3.height = 7
        self.assertEqual(r3.area(), 56)


class TestRectangleDisplay(unittest.TestCase):
    """Test cases for displaying the rectangle"""

    @staticmethod
    def capture_stdout(r, method):
        """Captures and returns text printed to stdout.
        Args:
            r (Rectangle): The rectangle printed to stdout.
            method: The function used to print a rectangle
        """
        capture = StringIO()
        sys.stdout = capture
        if method == "print":
            print(r)
        elif method == "display":
            r.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_width_height(self):
        r1 = Rectangle(2, 2)
        capture = TestRectangleDisplay.capture_stdout(r1, "display")
        expected = "##\n##\n"
        self.assertEqual(expected, capture.getvalue())

    def test_display_width_height_again(self):
        r2 = Rectangle(4, 6)
        capture = TestRectangleDisplay.capture_stdout(r2, "display")
        expected = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(expected, capture.getvalue())

    def test_display_width_height_x_y(self):
        r3 = Rectangle(2, 3, 2, 2)
        capture = TestRectangleDisplay.capture_stdout(r3, "display")
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(expected, capture.getvalue())

    def test_display_width_height_x_y_again(self):
        r4 = Rectangle(3, 2, 1, 0)
        capture = TestRectangleDisplay.capture_stdout(r4, "display")
        expected = " ###\n ###\n"
        self.assertEqual(expected, capture.getvalue())


class TestRectanglePrint(unittest.TestCase):
    """Test cases for printing the rectangle"""
    def test_str_width_height(self):
        r1 = Rectangle(4, 6)
        capture = TestRectangleDisplay.capture_stdout(r1, "print")
        expected = "[Rectangle] ({}) 0/0 - 4/6\n".format(r1.id)
        self.assertEqual(expected, capture.getvalue())

    def test_str_width_height_x(self):
        r2 = Rectangle(4, 6, 2)
        capture = TestRectangleDisplay.capture_stdout(r2, "print")
        expected = "[Rectangle] ({}) 2/0 - 4/6\n".format(r2.id)
        self.assertEqual(expected, capture.getvalue())

    def test_str_width_height_x_y(self):
        r3 = Rectangle(4, 6, 2, 1)
        capture = TestRectangleDisplay.capture_stdout(r3, "print")
        expected = "[Rectangle] ({}) 2/1 - 4/6\n".format(r3.id)
        self.assertEqual(expected, capture.getvalue())

    def test_str_width_height_x_y_id(self):
        r5 = Rectangle(4, 6, 2, 1, 12)
        capture = TestRectangleDisplay.capture_stdout(r5, "print")
        expected = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(expected, capture.getvalue())


if "__name__" == "__main__":
    unittest.main()
