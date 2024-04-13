#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """Template that represents a square"""

    def __init__(self, size=0):
        """Initializes a square instance

        Args:
            size (int): The size of the square
        """
        self.__size = size      # __ makes size a private instance

    @property
    def size(self):
        """Get the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size"""

        # Raise a Type Error if size is not an integer
        if type(value) is not int:
            raise TypeError("size must be an integer")

        # Raise a ValueError if size < 0
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value      # __ makes size a private instance

    def area(self):
        """"returns the current square area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        # if size is equal to 0, print an empty line
        if self.__size == 0:
            print()
        # Iterate throught the rows of the square
        for _ in range(self.__size):
            # print # size times in each row
            print("#" * self.__size)