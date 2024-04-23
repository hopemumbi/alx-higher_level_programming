#!/usr/bin/python3
"""Defines unittests for models/square.py
"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstatiation(unittest.TestCase):
    """ Test cases for the Square initialization """

    def test_inheritance(self):
        self.assertIsInstance(Square(2), Rectangle)

    def test_subclass(self):
        self.assertTrue(issubclass(Square, Base))


class TestSquareDisplay(unittest.TestCase):
    """Test for displaying a Square"""

    @staticmethod
    def capture_stdout(s, method):
        """Captures and returns text printed to stdout.
        Args:
            s (Square): The rectangle printed to stdout.
            method: Either print() or display()
        """
        capture = StringIO()
        sys.stdout = capture
        if method == "print":
            print(s)
        elif method == "display":
            s.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_size(self):
        s1 = Square(5)
        capture = TestSquareDisplay.capture_stdout(s1, "display")
        expected = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(expected, capture.getvalue())

    def test_str_size_x(self):
        s2 = Square(2, 2)
        capture = TestSquareDisplay.capture_stdout(s2, "display")
        expected = "  ##\n  ##\n"
        self.assertEqual(expected, capture.getvalue())

    def test_str_size_x_y(self):
        s3 = Square(3, 1, 3)
        capture = TestSquareDisplay.capture_stdout(s3, "display")
        expected = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(expected, capture.getvalue())


class TestSquareStr(unittest.TestCase):
    """Test cases for __str__ method of Square."""

    def test_str_size(self):
        s1 = Square(5)
        capture = TestSquareDisplay.capture_stdout(s1, "print")
        expected = "[Square] ({}) 0/0 - 5\n".format(s1.id)
        self.assertEqual(expected, capture.getvalue())

    def test_str_size_x(self):
        s2 = Square(2, 2)
        capture = TestSquareDisplay.capture_stdout(s2, "print")
        expected = "[Square] ({}) 2/0 - 2\n".format(s2.id)
        self.assertEqual(expected, capture.getvalue())

    def test_str_size_x_y(self):
        s3 = Square(3, 1, 3)
        capture = TestSquareDisplay.capture_stdout(s3, "print")
        expected = "[Square] ({}) 1/3 - 3\n".format(s3.id)
        self.assertEqual(expected, capture.getvalue())


class TestSquareArea(unittest.TestCase):
    """Test cases for the area of a square"""

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)


if __name__ == "__main__":
    unittest.main()
