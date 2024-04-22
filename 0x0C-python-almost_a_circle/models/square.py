#!/usr/bin/python3
""" Defines a Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes an instance of Square.

        Args:
            size (int): The width  and height of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identity of an instance of square..

        Raises:
            TypeError: If widt/x/y are not int`s.
            ValueError: : If either height or width are <= 0.
            ValueError: If x or y are < 0.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def area(self):
        """Return the area of a square"""
        return self.width * self.height

    def __str__(self):
        """Return a string representation of the Square instance.

        Overides the __str__ method

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update attributes
        Args:
            *args (ints): New attribute values.
                - id
                - size
                - x
                - y
            **kwargs (dict): key/value pairs
        """
        # If *args is provided and contains values
        if args and len(args) > 0:
            # Define the order of attributes to be updated
            attributes = ['id', 'width', 'height', 'x', 'y']
            # Iterate over the provided arguments and set attributes
            for i, attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])

        # If **kwargs is provided and contains key-value pairs
        elif kwargs and len(kwargs) > 0:
            # Iterate over the key-value pairs and set attributes accordingly
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        # Create a dictionary with instance attributes as key-value pairs
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
