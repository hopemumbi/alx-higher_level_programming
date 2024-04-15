#!/usr/bin/python3
"""This function takes an object obj as input
and returns the list of attributes and methods of that object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)
