#!/usr/bin/python3
class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes a square instance

        Args:
            size (int): The size of the square
        """
        # Raise a Type Error if size is not an integer
        if type(size) is not int:
            raise TypeError("size must be an integer")
        # Raise a ValueError if size < 0
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size      # __ makes size a private instance

    def area(self):
        """"returns the current square area

        Return:
            the area
        """
        return self.__size**2
