#!/usr/bin/python3
"""
Defines a Rectangle that inherits a base geometry class.
"""


class BaseGeometry:
    """Base class for geometry"""
    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is an integer greater than 0

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Derived class for rectangle"""
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
