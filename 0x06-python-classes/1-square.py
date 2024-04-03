#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initializes a square instance

        Args:
            size (int): The size of the square
        """
        self.__size = size      # __ makes size a private instance
