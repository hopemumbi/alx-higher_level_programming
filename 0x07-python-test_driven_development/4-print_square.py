#!/usr/bin/python3
"""Module for printing a square"""


def print_square(size):
    """ function that prints a square with the character #.

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If `size` is not an integer
        ValueError: Is size < 0

    """
    # TypeError: If `size` is not an integer
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Iterate through range(size) to print each row
    for _ in range(size):
        # Print a row of # characters of length `size`
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
