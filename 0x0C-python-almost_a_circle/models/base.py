#!/usr/bin/python3
"""Defines a class that is the base of all other classes in this project
    - that manages id attribute in all your future classes
    - avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """Represents a base"""

    # Private class attribute to keep track of the no of objects
    __nb_objects = 0

    # A constructor method
    def __init__(self, id=None):
        """ Initialize an instance of Base
        Attributes:
            id (int): optional assigns id to an instance
        """
        # If an id is provided
        if id is not None:
            # set the instance's id attribute to the provided id
            self.id = id
        # If no id is provided
        else:
            # increment the __nb_objects counter
            Base.__nb_objects += 1
            # and assign it as the id
            self.id = Base.__nb_objects
