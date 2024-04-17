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
        # If attribute list is provided,
        if attrs:
            #  Create an empty dictionary to store the JSON representation
            dictionary = {}
            for key in attrs:
                # Check if the key exists in the object's attributes list
                if hasattr(self, key):
                    # Add the key|value to then json dict
                    dictionary[key] = getattr(self, key)
        # If keys are not provided
        else:
            # Add all attributes
            dictionary = self.__dict__
        # Return the json dictionary
        return dictionary
