#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """Template that represents a square"""

    def __init__(self, size=0):
        """Initializes a square instance

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size"""

        # Raise a Type Error if size is not an integer
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        # Raise a ValueError if size < 0
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value      # __ makes size a private instance

    def area(self):
        """"returns the current square area

        Return:
            the area
        """
        return self.__size**2

    def __new__(cls, *args, **kwargs):
        instance = super(Square, cls).__new__(cls)
        return args[0] if args else 0
