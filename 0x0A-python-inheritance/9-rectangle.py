#!/usr/bin/python3
"""Defines a Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new rectangle

        Args:
            width (int) : width of the rectangle
            height (int) : height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
        Return the print()/str()/[informal] representation of a rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
