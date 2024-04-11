#!/usr/bin/python3
"""Module for printing name"""


def say_my_name(first_name, last_name=""):
    """Prints  My name is <first name> <last name>

    Args:
        first_name (str): the first name
        last_name (str): the last name

    Raises:
        TypeError: if arguments are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
