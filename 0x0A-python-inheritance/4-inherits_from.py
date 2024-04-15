#!/usr/bin/python3
"""A function that returns True if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a subclass"""
    # Cecks if the type of `obj` is different from `a_class`
    if type(obj) is not a_class:
        # Check if type of `obj` is the same as `a_class`
        return issubclass(type(obj), a_class)
