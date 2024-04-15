#!/usr/bin/python3
"""
Creates a class that reises an exception
"""


class BaseGeometry:
    """Raises an exception """
    def area(self):
        raise Exception("area() is not implemented")
