#!/usr/bin/python3
""" Write a function that adds 2 integers.

Attributes:
    add_integer(a, b=98): Add two integers
"""


def add_integer(a, b=98):
    """Returns the sum of 2 integers

    Args:
        a: The first parameter
        b: The second parameter

    Return:
        a+b :the sum of a and b
    """
    # a and b must be integers or floats
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    # a and b must be first casted to integers if they are float
    a = int(a) if isinstance(a, float) else a
    a = int(b) if isinstance(a, float) else a
    # Returns an integer: the addition of a and b
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
