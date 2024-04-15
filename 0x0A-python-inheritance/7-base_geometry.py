#!/usr/bin/python3
"""
Creates a class that validates an integer
"""


class BaseGeometry:
    """Base class for geometry"""
    def area(self):
        """Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
