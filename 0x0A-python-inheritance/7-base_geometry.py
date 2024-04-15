#!/usr/bin/python3
"""
Creates a class that reises an exception
"""


class BaseGeometry:
    """Raises an exception """
    def area(self):
        """Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
