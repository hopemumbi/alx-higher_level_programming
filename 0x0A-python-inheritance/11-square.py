#!/usr/bin/python3
"""Defines a class(Square) that inherits class(Rectangle)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, which is a special type of rectangle"""

    def __init__(self, size):
        """Initializes a new Square instance with a given size."""
        # Validate the size attribute
        self.integer_validator("size", size)
        # Initialize the Rectangle class and pass `size`
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the print() and str() description of a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
