#!/usr/bin/python3
"""Defines a class that is the base of all other classes in this project
    - that manages id attribute in all your future classes
    - avoid duplicating the same code (by extension, same bugs)
"""
import json


class Base:
    """Represents a base"""

    # Private class attribute to keep track of the no of objects
    __nb_objects = 0

    # A constructor method
    def __init__(self, id=None):
        """ Initialize an instance of Base
        Attributes:
            id (int): The identity of an instance of Base
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        # Check if the list of dictionaries is empty or None
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            # If so, return an empty list
            return "[]"
        # Otherwise, serialize the list of dictionaries to a JSON string
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base
        """
        # Filename must be: <Class name>.json
        filename = cls.__name__ + ".json"
        # Open the file in write mode, overwrite if it already exists
        with open(filename, 'w') as f:
            # If list_objs is None
            if list_objs is None:
                # Save an empty list
                f.write("[]")
            # If list_objs is not None
            else:
                # Convert each object to a dictionary representation
                list_dict = [obj.to_dictionary() for obj in list_objs]
                # Convert the list of dictionaries to a JSON string
                # And write it to file
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string representation to a list of dictionaries

        Args:
            json_string (str): A JSON string representing a list of dicts

        Returns:
             list: A list of dictionaries parsed from the JSON string.
        """
        # Check if json_string is None or empty
        if len(json_string) == 0 or json_string is None:
            # If so, return an empty list
            return []
        # Otherwise, parse the JSON sting and return a list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set
        based on the provided dictionary.

        Args:
            **dictionary: Key-value pairs for attributes and their values.
        """
        # create a dummy instance of the class Rectangle
        if cls.__name__ == 'Rectangle':
            # width and height set to default values (1, 1)
            dummy_instance = cls(1, 1)
        # create a dummy instance of the class Square
        if cls.__name__ == 'Square':
            # Size set to default value 1
            dummy_instance = cls(1)

        # use **dictionary as **kwargs to update the dummy_instance
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file."""
        # Filename must be: <Class name>.json
        filename = cls.__name__ + '.json'
        try:
            # If file exits, open it
            with open(filename, 'r') as f:
                # Read the data from the file
                data = f.read()
                # If data is not empty
                if data:
                    # Convert it from json_string then
                    obj_list = cls.from_json_string(data)
                    # Create instances from the list of dictionaries
                    return [cls.create(**obj) for obj in obj_list]
                else:
                    # If data is empty, return an empty list
                    return []
        except FileNotFoundError:
            # If the file doesn’t exist, return an empty list
            return []
