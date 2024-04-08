#!/usr/bin/python3
"""Module for Defining a rectangle"""


class Rectangle:
    """A class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height

       Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle

        Returns:
            Private instance attribute: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value (int) : The width to set. Must be an integer

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value` is negative
        """
        if not isinstance(value, int):  # or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle

        Returns:
            Private instance attribute: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value (int) : The height to set. Must be an integer

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value` is negative
        """
        if not isinstance(value, int):  # or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
