#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """Template that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance

        Args:
            size (int): The size of the square
        """
        self.__size = size      # __ makes size a private instance
        self.__position = position

    @property
    def size(self):
        """Get and set the value of size"""

        return self.__size

    @size.setter
    def size(self, value):
        # Raise a Type Error if size is not an integer
        if type(value) is not int:
            raise TypeError("size must be an integer")

        # Raise a ValueError if size < 0
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value      # __ makes size a private instance

    @property
    def position(self):
        """Get and set the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        # Raise a TypeError if position isn't a tuple of 2 positive integers
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """"returns the current square area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        # if size is equal to 0, print an empty line
        if self.__size == 0:
            print()
            return  # Exit the method early if size == 0

        # Don’t fill lines by spaces when position[1] > 0
        for _ in range(self.__position[1]):
            print()

        # Iterate throught the rows of the square
        for _ in range(self.__size):
            # print "#" size times and " " position[0] times
            print(" " * self.__position[0] + "#" * self.__size)
