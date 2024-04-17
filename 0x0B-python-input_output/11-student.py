#!/usr/bin/python3
"""A module defining the Student class"""


class Student:
    """ A class representing a student. """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary of attributes of the Student instance.
        """
        # If attrs is a list and all elements in attrs are strings
        if type(attrs) == list and all((type(key) == str for key in attrs)):
            # Create a dictionary
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        # If attrs is None or not a list or contains non-string elements
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance:

        """
        for k, v in json.items():
            setattr(self, k, v)
